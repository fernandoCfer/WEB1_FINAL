from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from requests import request
import imoveis
from .models import Imovel
from django.db.models import Q
from imoveis.forms import CadastroImovel, FormCategoria
from django.contrib.auth.decorators import login_required


class ImovelIndex(ListView):
    model = Imovel
    template_name = 'imoveis/index.html'
    paginate_by = 9
    context_object_name = 'imoveis'
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_imovel=True)
        
        return qs


class ImovelBusca(ImovelIndex):
    template_name = 'imoveis/imovel_busca.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        bairro = self.request.GET.get('bairro') 
        cat = self.request.GET.get('cat')
        
        if not bairro:
            return qs
        
        qs = qs.filter(
            Q(bairro_imovel__icontains=bairro) | 
            Q(rua_imovel__icontains=bairro) |
            Q(informacao_imovel=bairro)
        )
        
        return qs
    
    
class ImovelCategoriaBusca(ImovelIndex):
    template_name = 'imoveis/imovel_busca.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        bairro = self.request.GET.get('bairro') 
        categoria = self.kwargs.get('categoria', None)
        
        if not categoria or not bairro:
            return qs
        
        qs = qs.filter(categoria_imovel__nome_cat__iexact=categoria | Q(bairro_imovel__icontains=bairro))
        
        return qs


class ImovelCategoria(ImovelIndex):
    template_name = 'imoveis/imovel_categoria.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        categoria = self.kwargs.get('categoria', None)
        
        if not categoria:
            return qs
        
        qs = qs.filter(categoria_imovel__nome_cat__iexact=categoria)
        
        return qs
    


class ImovelDetalhes(UpdateView):
    template_name = 'imoveis/imovel_detalhes1.html'
    model = Imovel
    form_class = FormCategoria
    context_object_name = 'imovel'
    
    
    
def cadastro_imovel(request):
    if request.method != 'POST':
        return render(request, 'imoveis/cadastro_imovel.html')
    
    bairro = request.POST.get('bairro')
    logradouro = request.POST.get('logradouro')
    numero = request.POST.get('numero')
    tipo = request.POST.get('tipo')
    qtd_quartos = request.POST.get('qtd_quartos')
    garagem = request.POST.get('garagem')
    venda_aluguel = request.POST.get('venda_aluguel')
    av_rua = request.POST.get('av_rua')
    telefone = request.POST.get('telefone')
    m2 = request.POST.get('m2')
    qtd_banheiros = request.POST.get('qtd_banheiros')
    pets = request.POST.get('pets')
    quintal = request.POST.get('quintal')
    dinheiro = request.POST.get('dinheiro')
    complemento = request.POST.get('complemento')
    imagem = request.POST.get('imagem')
    
    form = Imovel(bairro_imovel=bairro, rua_imovel=logradouro, numero_imovel=numero, categoria_imovel=tipo, qtd_quartos_imovel=qtd_quartos,
                  garagem_imovel=garagem, venda_alugel_imovel=venda_aluguel, av_rua_imovel=av_rua, telefone_imovel=telefone, tamanho_imovel=m2,
                  qtd_banheiros_imovel=qtd_banheiros, pets_imovel=pets, quintal_imovel=quintal, preco_imovel=dinheiro, informacao_imovel=complemento,
                  imagens_imovel=imagem)
    form.save()
    
    #form = CadastroImovel(request.POST)
    
    #form = CadastroImovel(request.POST)
    #if form.is_valid():
        
    messages.success(request, 'Imóvel cadastrado com sucesso! faça login.')
    
    return redirect('index')  
