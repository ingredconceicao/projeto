from django.db import models

# Create your models here.
class Carros(models.Model):
    tipo = models.CharField(max_length=150)
    cor = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=150)
    ano = models.IntegerField()
    estado = models.CharField(max_length=100)
    km = models.CharField(max_length=100)
    passagem = models.CharField(max_length=100)
    pagamento = models.CharField(max_length=100)