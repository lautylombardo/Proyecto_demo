from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def miPlantilla(request):
    return render(request, "AppCoder/miPlantilla.html")
