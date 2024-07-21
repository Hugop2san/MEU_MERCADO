import hashlib
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect , get_object_or_404
from .models import Usuario, Produto, ListaDeCompra
from .forms import UsuarioForm,  LoginForm, ProdutoForm
from django.db.models import Count
from django.contrib import messages
from .forms import ListaDeCompraForm



# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_criptografada = hashlib.sha256(password.encode('utf-8')).hexdigest()
            
            try:
                usuario = Usuario.objects.get(email=email, password=password_criptografada )
                if usuario :
                    request.session['usuario_id'] = usuario.id
                    return redirect('dashboard')
            
            except Usuario.DoesNotExist:
                form.add_error(None, 'Email ou senha incorretos.')
        else:
            return render(request, 'usuarios/login.html', {'form': form})   
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


def registro(request):
    if request.method =='POST':
        form =UsuarioForm(request.POST)
        if form.is_valid():
            usuario= form.save(commit=False)
            
            if usuario.password:
                usuario.password = hashlib.sha256(usuario.password.encode('utf-8')).hexdigest()
                usuario.save()
                return redirect('login')        
            else:
                return render(request,'usuarios/registro.html', {'form': form})
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/registro.html', {'form':form})



def dashboard(request):
    usuario_id= request.session.get('usuario_id')
    if usuario_id :
        usuario= Usuario.objects.get(id = usuario_id)
        #lista_produtos = Produto.objects.filter(usuario = usuario)
        return render(request, 'listadecompra/dashboard.html', { 'usuario': usuario })
    else: 
        return redirect('login')
    
    
def criar_lista_de_compra(request):
    if request.method == 'POST':
        form = ListaDeCompraForm(request.POST)
        if form.is_valid():
            lista_de_compra = form.save(commit=False)
            lista_de_compra.usuario = request.user
            lista_de_compra.save()
            return redirect('criar_lista_de_compra')  # Redireciona para a pagina de criar lista e continuar adicionando.
    else:
        form = ListaDeCompraForm()
    return render(request, 'listadecompra/criar_lista_de_compra.html', {'form': form})
    
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('criar_lista_de_compra')  
    else:
        form = ProdutoForm()
    return render(request, 'usuarios/cadastrar_produto.html', {'form': form})


def listar_usuarios(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        usuario = Usuario.objects.get(id = usuario_id)
        if usuario.is_admin:
            usuarios = Usuario.objects.filter(is_admin=False)
            return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})
        else:
            messages.error(request, 'Você nao tem permissao para acessar essa pagina.')
            return redirect('dashboard')
    
    else: 
        return redirect('login')




def logout(request):
    request.session.flush()
    return redirect('login')

