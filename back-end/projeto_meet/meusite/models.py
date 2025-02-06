from django.db import models

# Create your models here.

class meusite(models.Model):
    nome = models.CharField(max_length=50)
    data_hora_agendamento = models.DateTimeField(null = True, blank = True)

class agenda(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    servico = models.CharField(max_length=100, blank= False, null= False)
    data_marcada = models.DateField(blank=False, null=False)
    horario_marcado = models.TimeField(blank=False, null=False)

    data_criacao = models.DateField(auto_now_add=True)
    
    def __str__(self):

        return f"cliente: {self.nome} serviço: {self.servico} para o dia {self.data_marcada} as {self.horario_marcado}"
    

