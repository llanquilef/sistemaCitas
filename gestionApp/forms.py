from django import forms
from .models import Cita

class CitaFormulario(forms.ModelForm):
    nombre_cliente = forms.CharField(label="Nombre y Apellido", max_length=100, required=True)
    numero_cliente = forms.CharField(label="Número de Teléfono", max_length=15, required=True)
    mail_cliente = forms.EmailField(label="Correo Electrónico", required=True)
    
    fechaHora = forms.DateTimeField(
        label="Fecha y Hora de la Cita",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        required=True
    )

    class Meta:
        model = Cita
        fields = ['estilista', 'servicio', 'fechaHora']
        widgets = {
            'estilista': forms.Select(attrs={'class': 'form-control'}),
            'servicio': forms.Select(attrs={'class': 'form-control'}),
        }
