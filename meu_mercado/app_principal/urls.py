from django.contrib import admin
from django.urls import path
from . import views
#path('app_principal/', include('app_principal.urls')),

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('criar_lista_de_compra/', views.criar_lista_de_compra, name='criar_lista_de_compra'),
    path('cadastrar_produto/', views.cadastrar_produto, name='cadastrar_produto'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('excluir_usuario/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),
    path('logout/', views.logout, name='logout'),

   
]

