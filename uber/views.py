from django.shortcuts import render
from django.http import HttpResponse


def v_iniciouber(request):

    return render(request, 'Uber/paginas/index.html')

def v_mobile(request):

    return render(request, 'Uber/paginas/mobile.html')

def v_contato(request):

    return render(request, 'Uber/paginas/contato.html')

def v_login(request):

    return render(request, 'Uber/paginas/login.html')

def v_registerMoto(request):

    return render(request, 'Uber/paginas/register_motorista.html')

def v_register(request):

    return render(request, 'Uber/paginas/register.html')

def v_servicos(request):

    return render(request, 'Uber/paginas/servicos.html')

def v_sobre(request):

    return render(request, 'Uber/paginas/sobre.html')

def v_eats(request):

    return render(request, 'Uber/paginas/uber_eats.html')

