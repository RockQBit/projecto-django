from random import random
from re import template
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from modelo.models import Persona
def viewer(request):
    return HttpResponse('hola como estas?')
def fecha(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"la fecha es {fecha_hora}")

def calcular_nacimiento(request, edad):
    nacimiento = datetime.now().year - edad
    return HttpResponse(f"tu año de nacimiento aproximado segun tu {edad} es: {nacimiento}")

def mi_template(request, nombre):
    # cargar_archivo = open(r'C:\Users\oreja\Desktop\project-django\templates\template.html')
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    # contexto = Context({'persona': nombre})
    # template_renderizado = template.render(contexto)
    template = loader.get_template('tu_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)
    
def prueba_template(request):
    # cargar_archivo = open(r'C:\Users\oreja\Desktop\project-django\templates\template.html')
    # template = Template(cargar_archivo.read())
    # cargar_archivo.close()
    # contexto = Context({'persona': nombre})
    # template_renderizado = template.render(contexto)
    mi_contexto = {'rango': list(range(1,11))}
    template = loader.get_template('prueba.html')
    template_renderizado = template.render(mi_contexto)
    return HttpResponse(template_renderizado)

def crear_persona(request, nombre, apellido, documento, edad):
    persona = Persona(nombre=nombre, apellido=apellido, documento=documento, edad =edad, fecha_nacimiento=datetime.now())
    persona.save()
    template = loader.get_template('crear_persona.html')
    template_renderizado = template.render({'personas': persona})
    return HttpResponse(template_renderizado)


def ver_personas(request):
    personas= Persona.objects.all()
    template = loader.get_template('ver_persona.html')
    template_renderizado = template.render({'personas': personas})
    return HttpResponse(template_renderizado)
