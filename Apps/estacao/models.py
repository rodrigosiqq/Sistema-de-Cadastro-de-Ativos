from django.db import models

# Create your models here.
class EstacaoTrabalho(models.Model):
    identificador=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=20)
    modelo=models.CharField(max_length=12)
    serial=models.CharField(max_length=20)
    setor=models.CharField(max_length=10)
    
    
