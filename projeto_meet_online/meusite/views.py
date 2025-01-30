from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html')

def pag_marcar(request):
    return render(request,'marcar_horario.html')
        