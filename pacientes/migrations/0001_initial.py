# Generated by Django 5.1.6 on 2025-02-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=255, null=True)),
                ('foto', models.ImageField(upload_to='fotos')),
                ('paganto_em_dia', models.BooleanField(default=True)),
                ('queixa', models.CharField(choices=[('TDAH', 'TDAH'), ('D', 'Depressão'), ('A', 'Ansiedade'), ('TAG', 'Transtorno de ansiedade generalizada')], max_length=4)),
            ],
        ),
    ]
