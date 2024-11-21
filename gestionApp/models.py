from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=64)
    rol = models.CharField(max_length=13, choices=[
        ('Cliente', 'Cliente'),
        ('Estilista', 'Estilista'),
        ('Administrador', 'Administrador'),
        ('Recepcionista', 'Recepcionista'),
    ])

    def __str__(self):
        return self.nombre


class Cliente(Usuario):
    historial_citas = models.JSONField(default=list, blank=True)
    numero_cliente = models.CharField(max_length=15)


class Estilista(Usuario): 
    agenda = models.JSONField(default=dict, blank=True)


class Recepcionista(Usuario):
    pass

class Administrador(Usuario):
    pass

class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    duracion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    estilista = models.ForeignKey(Estilista, on_delete=models.CASCADE, related_name='citas_estilista')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_citas')
    fechaHora = models.DateTimeField()
    estado = models.BooleanField(default=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='cita_servicios')

    def __str__(self):
        return f"Cita de {self.cliente} con {self.estilista} para {self.servicio} en {self.fechaHora}"


class CitaServicio(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE, related_name='servicios')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='cita_servicio')
