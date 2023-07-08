
from django.urls import path
from . import views

app_name = 'calculadora'

urlpatterns = [
    path('Home_Calculadora/',views.v_iniciocal, name='inicio'),
  

]


