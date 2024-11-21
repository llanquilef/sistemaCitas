from django.contrib import admin
from .models import Cliente, Estilista, Servicio, Cita

admin.site.register(Cliente)
admin.site.register(Estilista)
admin.site.register(Servicio)
admin.site.register(Cita)
