from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('reservaCita/', views.reserva_cita, name='reserva_cita'),  
    path('confirmacionCita/', views.confirmacion_cita, name='confirmacion_cita'),
]
