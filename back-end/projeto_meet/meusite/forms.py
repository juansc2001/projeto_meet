from .models import agenda,db_servico
from django import forms

class formulario_marcar_horario(forms.ModelForm):
    
    servico_disponiveis = db_servico.objects.all()
    SERVICOS_CHOICES = [
        ('', 'Selecione o serviço'),  # Opção padrão (desabilitada)
        
        ('corte', 'corte de cabelo')
    ]
    for dado in servico_disponiveis:
        SERVICOS_CHOICES.append((dado.id, dado.servico))


    servico = forms.ChoiceField(
        choices=SERVICOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )


    class Meta: 

        model = agenda
        fields = ['nome','servico','data_marcada','horario_marcado','horas_ocupadas']

        labels = {
            'nome': 'nome:',
            'servico': 'serviço:',
            'data_marcada' : 'data:',
            'horario_marcado' : 'horario de inicio:',
            'horas_ocupadas':'quantas horas o serviço vai levar',
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Digite seu nome"}),
            'data_marcada': forms.DateInput (attrs={'type':'date', 'class':'form-control'}),
            'horario_marcado' : forms.TimeInput(attrs={'type':'time', 'class':'form-control'}),
        }








class formulario_serviços (forms.ModelForm):
    class Meta:
        model = db_servico
        fields = ['servico','total_horas']

    labels={
        'servico':'serviço prestado: ',
        'total_horas':'duração do serviço: ',
    }