
from django.urls import path
from . import views

app_name = 'uber'

urlpatterns = [
    path('Home_Uber/',views.v_iniciouber,name='home'),
    path('Contato/',views.v_contato,name='contato'),
    path('Login/',views.v_login,name='login'),
    path('Mobile/',views.v_mobile,name='mobile'),
    path('Register_Motorista/',views.v_registerMoto,name='registerMoto'),
    path('Register/',views.v_register,name='register'),
    path('Servicos/',views.v_servicos,name='servicos'),
    path('Sobre/',views.v_sobre,name='sobre'),
    path('Uber_Eats/',views.v_eats,name='eats'),
    
    

 



  

]


