from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)

class Produto (models.Model):
    nome=models.CharField(max_length=50)
    categoria= models.CharField(max_length=50)
    cliente=models.OneToOneField(Cliente, on_delete=models.CASCADE)
class CarrinhoDeCompras (models.Model):
    nome=models.CharField(max_length=10)
    sexo=models.CharField(max_length=20)
    produto=models.ForeignKey(Produto, on_delete=models.CASCADE)
    

# Create your models here.
