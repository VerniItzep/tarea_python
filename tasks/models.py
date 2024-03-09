from django.db import models

class Task(models.Model):
    # Define other fields here
    Carnet = models.CharField(max_length=100, default='valor_predeterminado')
    Nombres = models.CharField(max_length=100, default='valor_predeterminado')
    Apellidos = models.CharField(max_length=100, default='valor_predeterminado')
    correoElectronico = models.EmailField(default='correo@ejemplo.com')
    fechaNacimiento = models.DateField(default='2024-01-01')


    def __str__(self):
        return self.Carnet
