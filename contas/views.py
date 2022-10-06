from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from imoveis.views import Imovel
from .forms import UserForm
#from django.http import 


# Create your views here.
def login(request):
    if request.method != 'POST':
        return render(request, 'contas/login.html')
    
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.error(request, 'usuário ou senha inválidos.')
        return render(request, 'contas/login.html')
    else:
        auth.login(request, user)
        return redirect('index')
    

def logout(request):
    auth.logout(request)
    return redirect('index')


def cadastro(request):
    if request.method != 'POST':
        return render(request, 'contas/cadastro.html')

    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    usuario = request.POST.get('usuario')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('conf_senha')
    
    try: 
        validate_email(email)
    except:
        messages.error(request, 'e-mail inválido.')
        return render(request, 'contas/cadastro.html')
    
    if len(senha) < 5:
        messages.error(request, 'senha precisa ter mais de 5 dígitos.')
        return render(request, 'contas/cadastro.html')
    
    if senha != senha2:
        messages.error(request, 'senhas não conferem. digite novamente.')
        return render(request, 'contas/cadastro.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'e-mail já existe. tente novamente.')
        return render(request, 'contas/cadastro.html')
    
    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'usuário já existe. tente novamente.')
        return render(request, 'contas/cadastro.html')
    
    if not nome or not email or not senha or not senha2 or not sobrenome or not usuario:
        messages.error(request, 'nenhum campo pode estar vazio, preencha-o(s).')
        return render(request, 'contas/cadastro.html')
    
    messages.success(request, 'cadastrado(a) com sucesso! faça login.')
    
    user = User.objects.create_user(username=usuario, first_name=nome, last_name=sobrenome, email=email, password=senha)
    user.save()
    
    return redirect('login')



@login_required(redirect_field_name='login.html')
def dashboard(request):
    return render(request, 'contas/dashboard.html')



@ login_required
def favorito_add(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    if imovel.favoritos.filter(id=request.user.id).exists():
        messages.success(request, f'Imóvel {id} removido da sua lista de favoritos.')
        imovel.favoritos.remove(request.user)
    else:
        messages.success(request, f'Imóvel {id} adicionado à sua lista de favoritos.')
        imovel.favoritos.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



@ login_required
def favoritos_lista(request):
    novo = Imovel.newmanager.filter(favoritos=request.user)
    return render(request, 'contas/favoritos.html', {'novo': novo})



def atualizar_dados(request, user_id):
    user = User.objects.get(pk=user_id,)
    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            user1 = form.save(commit=False)
            user1.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('dashboard')
        else:
            print('error.')
    return render(request, 'contas/dashboard.html')