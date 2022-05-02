from distutils.command.upload import upload
import email
from email.policy import default
from django.db import models
from django.utils import timezone

"""
CONTATOS
id: INT (automático)
nome: STR * (obrigatórioz
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criacao: DATETIME (automático)
descricao: texto
categoria: CATEGORIA (outro model)

CATEGORIA
id: INT
nome: STR * (obrigatório)
"""


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True) # opcional
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True) # opcional
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    #%Y/%m/%d cria uma pasta com ano, mes, dia
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')  

    def __str__(self):
        return self.nome
