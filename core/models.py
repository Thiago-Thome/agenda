from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_criacao = models.DateField(auto_now=True, verbose_name='Data de criação')
    data_evento = models.DateField(verbose_name='Data do evento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:  # cira tabela com nome da classe (evento).
        db_table = 'evento'

    def __str__(self):   # força o titulo no campo evento
        return self.titulo
