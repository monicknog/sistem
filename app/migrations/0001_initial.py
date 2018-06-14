# Generated by Django 2.0.4 on 2018-05-25 13:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acesso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data Acesso')),
                ('hora_entrada', models.TimeField(blank=True, null=True, verbose_name='Entrada')),
                ('hora_saida', models.TimeField(blank=True, null=True, verbose_name='Saída')),
                ('total_horas', models.DurationField(blank=True, null=True, verbose_name='Total')),
            ],
            options={
                'verbose_name': 'Acesso',
                'verbose_name_plural': 'Acessos',
            },
        ),
        migrations.CreateModel(
            name='Bolsista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('matricula', models.CharField(max_length=100, unique=True, verbose_name='Matricula')),
                ('cartao_rfid', models.CharField(max_length=100, null=True, verbose_name='Cartão RFID')),
                ('tipo_bolsa', models.IntegerField(choices=[(0, 'Voluntário'), (1, 'Remunerado')], verbose_name='Tipo')),
                ('carga_horaria_semanal', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Carga Horaria (semanal)')),
            ],
            options={
                'verbose_name': 'Bolsista',
                'verbose_name_plural': 'Bolsistas',
            },
        ),
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Orientador',
                'verbose_name_plural': 'Orientadores',
            },
        ),
        migrations.AddField(
            model_name='bolsista',
            name='orientador',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='bolsista_professor', to='app.Orientador', verbose_name='Orientador'),
        ),
        migrations.AddField(
            model_name='acesso',
            name='bolsista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bolsista_acesso', to='app.Bolsista', verbose_name='Bolsista'),
        ),
    ]
