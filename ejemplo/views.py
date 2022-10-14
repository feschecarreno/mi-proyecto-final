from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre": "Federico", "apellido": "Carreño"})#paso un diccionario

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",{"nombre": nombre, "apellido": apellido})#paso un diccionario

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    { "notas":[1,2,3,4,5,6,7]})

def imc (request, peso, altura):
    imc = peso / ((altura/100)**2)
    return render (request, "ejemplo/saludar.html",
    {"peso": peso,
    "altura": altura,
    "imc": imc,
    })

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

  