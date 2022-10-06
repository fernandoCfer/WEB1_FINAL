from django.urls import path
from . import views


urlpatterns = [
    path('', views.ImovelIndex.as_view(), name='index'),
    path('categoria/<str:categoria>', views.ImovelCategoria.as_view(), name='imoveis_categoria'),
    path('categoria/<str:categoria>/busca/', views.ImovelCategoriaBusca.as_view(), name='imoveis_categoria_busca'),
    path('busca/', views.ImovelBusca.as_view(), name='imoveis_busca'),
    path('imovel/<int:pk>', views.ImovelDetalhes.as_view(), name='imoveis_detalhes'),
    path('cadastro/', views.cadastro_imovel, name='cadastro_imovel'),
]