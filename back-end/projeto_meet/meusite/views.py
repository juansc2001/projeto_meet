from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import formulario_marcar_horario, formulario_serviços
from .models import agenda, db_servico
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    return render(request,'index.html')

def pag_marcar(request):
    form = formulario_marcar_horario(request.POST)
    if request.method == 'POST':    
            if( form.is_valid()):
                data_marcada = form.cleaned_data['data_marcada']
                horario_marcado_formulario = form.cleaned_data['horario_marcado']
                

                if agenda.objects.filter(data_marcada=data_marcada).exists():#se encontro for marcado no mesmo dia
                    hora_nao_ocupada = True

                    objeto_agenda = agenda.objects.all()
                    for objetos in objeto_agenda:
                        horario_inicio = objetos.horario_marcado
                        horario_inicio_com_data = datetime.combine(datetime.today(),horario_inicio)
                        horario_fim = horario_inicio_com_data + timedelta(hours = objetos.horas_ocupadas)
                        horario_marcado_formulario_com_data = datetime.combine(datetime.now(), horario_marcado_formulario)

                        if(horario_inicio_com_data <= horario_marcado_formulario_com_data <= horario_fim ):
                             print("este horario ja esta marcado")
                             print(f"horario inicio {horario_inicio_com_data} até {horario_fim} \n vc marcou para as {horario_marcado_formulario_com_data}")
                             hora_nao_ocupada = False
                    
                    if hora_nao_ocupada:
                        form.save()
                        return redirect(home)
                    else:
                        form.add_error(None,'este horario ja tem um encontro marcado')
                else:
                    form.save()
                    return redirect(home)
            else:
                form.add_error(None,'dados invalidos')   
    else:
        form = formulario_marcar_horario()

    return render(request,'marcar_horario.html',{ 'formulario_agendamento': form })




def agendado(request):
    data = agenda.objects.all()
    return render(request,'agendado.html', {'dados_agendados' : data})



def configurar_servico(request):
    formulario_serv = formulario_serviços(request.POST)
    if request.method == 'POST': 
            if formulario_serv.is_valid():
                formulario_serv.save()
                return redirect(home)
            else:
                formulario_serv.add_error(None,'dados invalidos')
    else:
        formulario_serv = formulario_serviços()
        
    return render(request, 'configurar_servico.html', {'formulario': formulario_serv })