from django.shortcuts import render


def index(request):
    return render(request, "ejemplo/saludar.html",{"nombre": "Federico", "apellido": "Carreño"})#paso un diccionario

def index_dos(request, nombre, apellido):
    return render(request, "ejemplo/saludar.html",{"nombre": nombre, "apellido": apellido})#paso un diccionario

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    { "notas":[1,2,3,4,5,6,7]})