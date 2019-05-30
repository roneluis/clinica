from django.db import models

class Paciente (models.Model):
    nome = models.CharField(max_length = 50)
    dt_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1)

class Medico (models.Model):
    nome = models.CharField(max_length = 50)
    crm = models.CharField(max_length = 40)
    especialidade = models.CharField(max_length = 40)
    idade = models.IntegerField()