from django.shortcuts import render,redirect
from .models import EstacaoTrabalho


# Create your views here.
def home(request):
    ativos = EstacaoTrabalho.objects.all()
    return render(request, "GestaoEstacoes.html", {"ListarAtivos": ativos})

def registrarEstacao(request):
    nome = request.POST['txtNome']
    modelo = request.POST['txtmodelo']
    serial = request.POST['txtserial']
    setor = request.POST['txtsetor']
    
    estacao = EstacaoTrabalho.objects.create(nome=nome, modelo=modelo, serial=serial, setor=setor)
    return redirect('/')

def deletarEstacao(resquest, identificador):
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    estacao.delete()
    return redirect('/')
    
    
    
    