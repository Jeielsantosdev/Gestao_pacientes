# Generated by Django 5.1.6 on 2025-02-19 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='paganto_em_dia',
            new_name='pagando_em_dia',
        ),
    ]
