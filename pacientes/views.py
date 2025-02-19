from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Paciente, Tarefas, Consultas, Visualizacoes
from django.contrib import messages
from django.contrib.messages import constants


def pacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        print(pacientes)


        return render(request, 'pacientes.html',{'queixas':Paciente.queixa_choices, 'pacientes':pacientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto:
            messages.add_message(request,constants.ERROR, 'Preencha todos os campos')
            return redirect('pacientes') 

        pacientes = Paciente(
            nome = nome,
            email = email,
            telefone = telefone,
            queixa = queixa,
            foto = foto
        )

        pacientes.save()
        messages.add_message(request,constants.SUCCESS, 'Cadastro realizado com sucesso')
        return redirect('pacientes')

def paciente_view(request, id):
    paciente = Paciente.objects.get(id=id)
    if request.method == "GET":
        tarefas = Tarefas.objects.all()
        consultas = Consultas.objects.filter(paciente=paciente)

    
        tuple_grafico = ([str(i.data) for i in consultas], [str(i.humor) for i in consultas])
        
        return render(request, 'paciente.html',{'paciente':paciente, 'tarefas':tarefas, 'consultas':consultas,'tuple_grafico':tuple_grafico})
    elif request.method == 'POST':
        humor = request.POST.get('humor')
        registro_geral = request.POST.get('registro_geral')
        video = request.POST.get('video')
        tarefas = request.POST.getlist('tarefas')
        
        consultas = Consultas(
            humor = int(humor),
            registro_geral=registro_geral,
            video=video,
            paciente=paciente
        )
        consultas.save()

        for i in tarefas:
            tarefas= Tarefas.objects.get(id=i)
            consultas.tarefas.add(tarefas)
        consultas.save()


        messages.add_message(request,constants.SUCCESS, 'Cadastro realizado com sucesso')
        return redirect(f'/pacientes/{id}')


def atualizar_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    pagamento_em_dia = request.POST.get('pagamento_em_dia')
    status = True if pagamento_em_dia == 'ativo' else False
    paciente.pagamento_em_dia = status
    paciente.save()
    return redirect(f'/pacientes/{id}')

def excluir_consulta(request, id):
    consulta = Consultas.objects.get(id=id)
    consulta.delete()
    return redirect(f'/pacientes/{consulta.paciente.id}')

def consulta_publica(request,id):
    consulta = Consultas.objects.get(id=id)
    if not consulta.paciente.pagando_em_dia:
        raise Http404()
    
    return render(request, 'consulta_publica.html',{'consulta':consulta})


@property
def views(self):
    views = Visualizacoes.objects.filter(consulta=self)
    totais = views.count()
    unicas = views.values('ip').distinct().count()
    return f'{totais} - {unicas}'