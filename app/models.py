from django.db import models

class Cliente (models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    idade = models.IntegerField(null=True, blank=True)
    data_nascimento = models.DateField(null=False, blank=False)
    is_ativo = models.BooleanField(null=False, default=True)