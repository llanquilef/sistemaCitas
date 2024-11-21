from django.shortcuts import render, redirect
from .models import Cita, Cliente
from .forms import CitaFormulario

def Index(request):
    return render(request, 'index.html')

def reserva_cita(request):
    if request.method == 'POST':
        form = CitaFormulario(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cliente, created = Cliente.objects.get_or_create(
                nombre= request.POST.get('nombre_cliente'),
                numero_cliente =request.POST.get('numero_cliente'),
                correo= request.POST.get('mail_cliente'),
                defaults={
                    'rol': 'Cliente'
                    }
            )
            
            cita.cliente = cliente
            cita.save() 
            return redirect('confirmacion_cita')
    else:
        form = CitaFormulario()

    return render(request, 'gestionApp/citaReserva.html', {'form': form})

def confirmacion_cita(request):
    return render(request, 'gestionApp/citaConfirmacion.html')

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'gestionApp/listaCitas.html', {'citas':citas})
