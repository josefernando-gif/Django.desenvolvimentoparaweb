from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mae = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, default='', blank=True)
    celular = models.CharField(max_length=15)
