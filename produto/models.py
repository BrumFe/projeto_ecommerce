from django.conf import settings
import os
from PIL import Image
from django.db import models
from django.utils.text import slugify
from utils import utils


# Create your models here.


class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_produto = models.TextField(
        max_length=1000, verbose_name='Descrição')
    descricao_tecnica = models.TextField(
        max_length=25000, verbose_name='Ficha Técnica')
    marca = models.CharField(max_length=155,)
    modelo = models.CharField(max_length=155)
    qualidade_equipamento = models.CharField(
        default='N',
        max_length=1,
        choices=(
            ('N', 'Novo'),
            ('S', 'Seminovo (até 4 meses de uso)'),
            ('U', 'Usado'),
        ), verbose_name='Qualidade do produto'
    )
    # TODO: Remove blank and null
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    imagem_1 = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    imagem_2 = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    imagem_3 = models.ImageField(
        upload_to='produto_imagens/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name='Preço Promo')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        return utils.formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'

    def get_preco_promocional_formatado(self):
        return utils.formata_preco(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = 'Preço Promo'

    """
    Método de redimensionamento de imagem
    """

    # TODO: Pode ser movida para um arquivo único e reutilizada em outros models, caso necessário.

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
