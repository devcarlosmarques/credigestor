from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Proposta, Noticia
from django.contrib.auth import authenticate, login, logout

def cadastro(request):
    if request.method == 'POST':
        campo_nome = request.POST.get('campo_nome')
        campo_login = request.POST.get('campo_login')
        campo_senha = request.POST.get('campo_senha')
        campo_email = request.POST.get('campo_email')
        campo_cargo = request.POST.get('campo_cargo')

        # Verificar se já existe um usuário com o mesmo nome de usuário
        if User.objects.filter(username=campo_login).exists():
            messages.error(request, 'Nome de usuário já existe. Escolha outro nome.')
            return redirect('cadastro')

        # Criar uma nova instância de User
        novo_usuario = User.objects.create_user(
            username=campo_login,
            password=campo_senha,
            email=campo_email,
            first_name=campo_nome,
            is_superuser=campo_cargo,
        )

        messages.success(request, 'Usuário cadastrado com sucesso.')

        return redirect('login')

    return render(request, 'cadastro/cadastro_usuario.html')


def fazer_login(request):
    if request.method == 'POST':
        username = request.POST.get('campo_login')
        password = request.POST.get('campo_senha')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,f'Usuário {username}, logado com sucesso!')
            return redirect('home')
        else:
            messages.error(request,'Credenciais incorretas, tente novamente.')
            return render(request, 'login/index.html')

    return render(request, 'login/index.html')

def home(request):
    return render(request,'dashboard/noticias.html')

def cadastro_proposta(request):
    
    if request.method == 'POST':
        
        bd = Proposta()
        bd.nome = request.POST.get('campo_nome')
        bd.cpf = request.POST.get('campo_cpf')
        bd.proposta = request.POST.get('campo_proposta')
        bd.orgao = request.POST.get('campo_orgao')
        bd.operacao = request.POST.get('campo_operacao')
        bd.banco = request.POST.get('campo_banco')
        bd.valor = request.POST.get('campo_valor')
        bd.parcela = request.POST.get('campo_parcela')
        bd.prazo = request.POST.get('campo_prazo')
        bd.status = request.POST.get('campo_status')
        bd.save()

        messages.success(request, f'Proposta {bd.proposta} cadastrada com sucesso!')
        return redirect('home')

    return render(request, 'cadastro/cadastro_proposta.html')

def consultar_proposta(request):
    lista_proposta = Proposta.objects.all()
    return render(request,'consultar/consultar_proposta.html', {'lista_proposta':lista_proposta})

def fazer_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema!')
    return redirect('login')

def noticias(request):
    lista_noticia = Noticia.objects.all()
    return render(request,'dashboard/noticias.html', {'lista_noticia':lista_noticia})

def consultar_usuario(request):
    lista_usuario = User.objects.all()
    return render(request,'consultar/consultar_usuario.html', {'lista_usuario':lista_usuario})