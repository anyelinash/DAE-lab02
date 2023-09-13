from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
     path('calculadora', views.calcular, name='calcular'), 
    path('resultado', views.resultado, name='resultado'),
    path('cilindro', views.calvolumen, name='calvolumen'),
]

