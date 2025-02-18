# Generated by Django 5.1.4 on 2025-01-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuestionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='escalavaloracion',
            name='id_dimension',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='id_dimension',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='escalavaloracion',
            table='escalas_valoracion',
        ),
        migrations.AlterModelTable(
            name='gradoescolar',
            table='grados_escolares',
        ),
        migrations.AlterModelTable(
            name='pregunta',
            table='preguntas',
        ),
    ]
