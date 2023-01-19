from django.db import models

class TodoList(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.CharField(
        "Descripción",
        blank=True,
        max_length=100,
        help_text="Descripción de la lista de tareas",
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Lista de tareas"
        verbose_name_plural = "Listas de tareas"

class Todo(models.Model):
    title = models.CharField("Titulo", max_length=50, help_text="Titulo de la tarea")
    description = models.TextField("Descripción", help_text="Descripción de la tarea")
    is_completed = models.BooleanField("Completado", default=False)
    is_deleted = models.BooleanField("Eliminado", default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # Acerca de la clase Meta:  https://docs.djangoproject.com/en/1.11/ref/models/options/
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
