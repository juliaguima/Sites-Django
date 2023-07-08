from django.shortcuts import render
from django.http import HttpResponse

def v_inicioor(request):

    return render(request,'orcamento/paginas/index.html')


def v_cons(request):

    return render(request,'orcamento/paginas/consulta.html')

