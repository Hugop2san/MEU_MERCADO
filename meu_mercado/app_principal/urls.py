from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('criar_lista_de_compra/', views.criar_lista_de_compra, name='criar_lista_de_compra'),
]

