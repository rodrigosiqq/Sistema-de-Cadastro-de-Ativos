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

def edicaoEstacao(request, identificador):
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    return render(request, "edicaoEstacao.html", {"estacao": estacao})
    

def editarEstacao(request, identificador):
    
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    
    estacao.nome = request.POST['txtNome']
    estacao.modelo = request.POST['txtmodelo']
    estacao.serial = request.POST['txtserial']
    estacao.setor = request.POST['txtsetor'] 
    # estacao = EstacaoTrabalho.objects.update_or_create(identificador=id, nome=nome, modelo=modelo, serial=serial, setor=setor)
    estacao.save()
    return redirect('/')
    
        


def deletarEstacao(resquest, identificador):
    estacao = EstacaoTrabalho.objects.get(identificador=identificador)
    estacao.delete()
    return redirect('/')
    
    
    
    