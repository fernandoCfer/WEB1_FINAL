from django.contrib import admin
from .models import Imovel
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class ImovelAdmin(SummernoteModelAdmin):
    list_display = ('id', 'anunciante_imovel', 'bairro_imovel',
                    'rua_imovel', 'numero_imovel', 'telefone_imovel', 
                    'categoria_imovel', 'preco_imovel', 'publicado_imovel',)
    list_editable = ('publicado_imovel',)
    list_display_links = ('id', 'categoria_imovel',)
    summernote_fields = ('informacao_imovel')
    
    

admin.site.register(Imovel, ImovelAdmin)