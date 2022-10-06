from django.forms import ModelForm
from .models import Imovel


class FormCategoria(ModelForm):
    class Meta:
        model = Imovel
        fields = ('anunciante_imovel', 'data_imovel', 'bairro_imovel',
                  'numero_imovel', 'preco_imovel')
        
        

class CadastroImovel(ModelForm):
    class Meta:
        model = Imovel
        fields = ('anunciante_imovel', 'data_imovel', 'bairro_imovel', 'rua_imovel', 'numero_imovel', 'categoria_imovel', 'qtd_quartos_imovel', 'garagem_imovel', 'venda_alugel_imovel', 'av_rua_imovel', 'telefone_imovel', 'tamanho_imovel', 'qtd_banheiros_imovel', 'pets_imovel', 'quintal_imovel', 'preco_imovel', 'informacao_imovel', 'imagens_imovel')