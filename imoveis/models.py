from django.db import models
from categoria.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


SIM = 'Sim'
NAO = 'Não'
CHOICES_SIM_NAO = (
    (SIM, 'Sim'),
    (NAO, 'Não')
)

VENDA = 'Venda'
ALUGUEL = 'Aluguel'
CHOICES_VENDA_ALUGUEL = (
    (VENDA, 'Venda'),
    (ALUGUEL, 'Aluguel')
)

RUA = 'Rua'
AVENIDA = 'Avenida'
CHOICES_RUA_AVENIDA = (
    (RUA, 'Rua'),
    (AVENIDA, 'Avenida')
)

# Create your models here.
class Imovel(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(publicado_imovel=True)
    
    
    anunciante_imovel = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='anunciante')
    data_imovel = models.DateTimeField(default=timezone.now(), verbose_name='data')
    bairro_imovel = models.CharField(max_length=65, verbose_name='bairro')
    av_rua_imovel = models.CharField(max_length=7, verbose_name='av ou rua', choices=CHOICES_RUA_AVENIDA, default='')
    rua_imovel = models.CharField(max_length=100, verbose_name='rua')
    numero_imovel = models.IntegerField(verbose_name='número imovel')
    telefone_regex = RegexValidator(regex=r'(\(?\d{2}\)?\s)?(\d{4,5}\-\d{4})', message=_('error.'))
    telefone_imovel = models.CharField(validators=[telefone_regex], max_length=17) # Validators should be a list
    preco_imovel = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    categoria_imovel = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='categoria')
    tamanho_imovel = models.IntegerField()
    qtd_quartos_imovel = models.IntegerField()
    qtd_banheiros_imovel = models.IntegerField()
    garagem_imovel = models.CharField(verbose_name='garagem', choices=CHOICES_SIM_NAO, max_length=3)
    pets_imovel = models.CharField(verbose_name='pets', choices=CHOICES_SIM_NAO, max_length=3)
    quintal_imovel = models.CharField(verbose_name='quintal', choices=CHOICES_SIM_NAO, max_length=3, default='')
    venda_alugel_imovel = models.CharField(verbose_name='venda ou aluguel', choices=CHOICES_VENDA_ALUGUEL, max_length=7)
    informacao_imovel = models.TextField()
    imagens_imovel = models.ImageField(upload_to='imovel_img/%Y/%m/%d', blank=True, null=True)
    publicado_imovel = models.BooleanField(default=False)
    favoritos = models.ManyToManyField(User, related_name='favoritos', default=None, blank=True)
    manager = models.Manager()
    newmanager = NewManager()
    
    def __str__(self):
        return self.rua_imovel