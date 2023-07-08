
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/',admin.site.urls, ),
    path('', include('inicial.urls')),
    path('calculadora/', include('calculadora.urls')),
    path('Uber/', include('uber.urls')),
    path('Orcamento/', include('orcamento.urls')),


    
]


