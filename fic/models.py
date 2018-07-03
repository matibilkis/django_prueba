from django.db import models
from django.urls import reverse

class Alumno(models.Model):
    nombre = models.CharField(max_length=200, help_text="Nombre")
    apellido = models.CharField(max_length=200, help_text="Apellido")
    curso = models.CharField(max_length=200, help_text="Curso")

    def __str__(self):
        return self.nombre + ' '+ self.apellido

    def get_absolute_url(self):
        return reverse('alumno-detail', args=[str(self.id)])
