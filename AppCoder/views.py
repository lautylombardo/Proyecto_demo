from django.http import HttpResponse
from django.shortcuts import render

from Proyecto1.ProyectoCoder.AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre="Desarrollo wev", camada = "19881")
    curso.save()
    documentoDeTexto = f"C--->Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documentoDeTexto)
