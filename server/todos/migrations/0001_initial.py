# Generated by Django 4.1.5 on 2023-01-18 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Lista de tareas',
                'verbose_name_plural': 'Listas de tareas',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Titulo de la tarea', max_length=50, verbose_name='Titulo')),
                ('description', models.TextField(help_text='Descripción de la tarea', verbose_name='Descripción')),
                ('todo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todos.todolist')),
            ],
            options={
                'verbose_name': 'Tarea',
                'verbose_name_plural': 'Tareas',
            },
        ),
    ]
