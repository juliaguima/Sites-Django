from django.shortcuts import render
from django.http import HttpResponse


def v_host(request):

    return render(request,'inicial/paginas/home.html')
