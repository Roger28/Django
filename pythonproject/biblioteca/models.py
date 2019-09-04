from django.db import models
from django.utils import timezone

# Create your models here.
class Usuario(models.Model):
	matricula = models.CharField(max_length=20, primary_key=True)
	nome = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	endereco = models.CharField(max_length=100)
	telefone = models.CharField(max_length=20)

class Emprestimo(models.Model):
	codigo = models.CharField(max_length=20, primary_key=True)
	data_hora = models.DateTimeField('data emprestimo')
	matricula = models.ForeignKey(Usuario,on_delete=models.CASCADE)
	data_devolução = models.DateTimeField('data devolucao')

class Sessao(models.Model):
	codigo = models.CharField(max_length=20, primary_key=True)
	descricao = models.CharField(max_length=200)
	localizacao = models.CharField(max_length=200)

class Livro(models.Model):
	codigo = models.CharField(max_length=20, primary_key=True)
	titulo = models.CharField(max_length=50)
	autor = models.CharField(max_length=20)
	codigo_sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)
	emprestimo = models.ManyToManyField(Emprestimo)
