from django import forms
from .models import ListaDeCompra, Produto
from django.forms.widgets import SelectDateWidget
from app_principal.models import Usuario
from django.contrib.auth.hashers import make_password, check_password


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label          
            
            
            
class UsuarioForm(BootstrapModelForm):
    class Meta:
        model=Usuario 
        fields= ['nome','idade', 'email', 'password' ]
        widgets={
            'password': forms.PasswordInput(),
        }
    
class LoginForm(BootstrapModelForm):
        class Meta:
            model= Usuario
            fields= ['email', 'password']
            widgets= {
                'password': forms.PasswordInput(),
            }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'].widget.attrs['placeholder'] = 'exemplo@dominio.com'
            self.fields['password'].widget.attrs['placeholder'] = 'Sua senha'
      
        def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')

            if email and password:
                try:
                    user = Usuario.objects.get(email=email)
                    if not user.password:
                        raise forms.ValidationError('Senha incorreta.')
                except Usuario.DoesNotExist:
                    raise forms.ValidationError('Email não encontrado.')

            return cleaned_data  

      
class ListaDeCompraForm(forms.ModelForm):
    data = forms.DateField(widget=SelectDateWidget())
    produto = forms.ModelChoiceField(queryset=Produto.objects.all(), empty_label="---------")
    
    class Meta:
        model = ListaDeCompra
        fields = ['produto', 'data', 'quantidade', 'preco_unitario']

    def clean_preco(self):
        preco_unitario = self.cleaned_data.get('preco_unitario')
        if preco_unitario <= 0:
            raise forms.ValidationError("O preço deve ser um valor positivo.")
        return preco_unitario

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        if quantidade <= 0:
            raise forms.ValidationError("A quantidade deve ser um valor positivo.")
        return quantidade
    
    
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao']

