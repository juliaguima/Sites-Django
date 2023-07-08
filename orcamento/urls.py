
from django.urls import path
from . import views

app_name = 'orcamento'

urlpatterns = [
    
    path('Home_Orcamento/',views.v_inicioor, name='index'),
    path('Consulta/',views.v_cons, name='consulta'),

  

]


