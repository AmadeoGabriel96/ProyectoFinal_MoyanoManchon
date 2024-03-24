from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Curso(models.Model): 

    def __str__(self):
        
        return f"Nombre: {self.nombre} --- Camada: {self.camada}"

    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()

class Profesor(models.Model):

    def __str__(self):
        
        return f"Nombre: {self.nombre} --- Apellido: {self.apellido}"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()
    profesión = models.CharField(max_length=30)

class Alumno(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} --- Apellido: {self.apellido}"

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    email = models.EmailField()   

class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

    