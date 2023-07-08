from django.shortcuts import render
from django.http import HttpResponse

def v_iniciocal(request):

    return render(request, 'calculadora/paginas/inicio.html')



