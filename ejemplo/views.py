from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm
from django.views import View

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

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}# para que pongamos algo en el mensaje, (por ej ingrese contraseña)

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})