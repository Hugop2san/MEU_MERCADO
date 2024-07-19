from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Count
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'usuarios'
        db_table = 'usuario'
        verbose_name = 'usuario'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.nome
    
    def get_by_natural_key(self, email):
        return self.get(email=email)
     
    def is_anonymous(self):
        return False
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class ListaDeCompra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField()
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'listas_de_compra'
        db_table = 'lista_de_compra'
        verbose_name = 'lista de compra'
        ordering = ['-data']
    
    def __str__(self):
        return f"{self.usuario.nome} - {self.produto.nome} - {self.data}"