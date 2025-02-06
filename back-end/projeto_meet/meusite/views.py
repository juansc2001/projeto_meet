from django.shortcuts import render
from django.http import HttpResponse
from .forms import formulario_marcar_horario
from .models import agenda

# Create your views here.

def home(request):
    return render(request,'index.html')

def pag_marcar(request):

    

    if request.method == 'POST':
        form = formulario_marcar_horario(request.POST)
        if( form.is_valid()):
            form.save()
    else:
        form = formulario_marcar_horario()


    return render(request,'marcar_horario.html',{ 'formulario_agendamento': form })


def agendado(request):

    data = agenda.objects.all()

    return render(request,'agendado.html', {'dados_agendados' : data})