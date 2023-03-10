# Generated by Django 4.1.5 on 2023-01-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Completado'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='description',
            field=models.CharField(blank=True, help_text='Descripción de la lista de tareas', max_length=100, verbose_name='Descripción'),
        ),
    ]
