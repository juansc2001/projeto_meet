from .models import agenda
from django import forms

class formulario_marcar_horario(forms.ModelForm):
    
    SERVICOS_CHOICES = [
        ('', 'Selecione o serviço'),  # Opção padrão (desabilitada)
        ('corte', 'Corte de Cabelo'),
        ('trancas', 'Tranças'),
        ('barba', 'Barba'),
    ]
     
    servico = forms.ChoiceField(
        choices=SERVICOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )


    class Meta: 

        model = agenda

        fields = ['nome','servico','data_marcada','horario_marcado']

        labels = {
            'nome': 'nome:',
            'servico': 'serviço:',
            'data_marcada' : 'data:',
            'horario_marcado' : 'hora:',
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite seu nome"}),
            'data_marcada': forms.DateInput (attrs={'type':'date', 'class':'form-control'}),
            'horario_marcado' : forms.TimeInput(attrs={'type':'time', 'class':'form-control'}),
        }