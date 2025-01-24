from django.db import models

# Create your models here.

class meusite(models.Model):
    nome = models.CharField(max_length=50)
    data_hora_agendamento = models.DateTimeField(null = True, blank = True)
    