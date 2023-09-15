from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=256)
    valor = models.FloatField()
    data_de_validade=models.DateTimeField(blank=True, null=True)
    quantidade=models.IntegerField(default=0)
    quantidade2=models.IntegerField(default=0)