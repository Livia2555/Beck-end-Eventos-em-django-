from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=20)
    Descricao= models.CharField(max_length=100)
    DataHora= models.DateTimeField()
    Local= models.CharField(max_length=30)
    Categoria = models.CharField(max_length=20)

    def ___str__(self):
        return self.nome
