from django.contrib import admin
from .models import Paciente, Tarefas, Consultas
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Tarefas)
admin.site.register(Consultas)