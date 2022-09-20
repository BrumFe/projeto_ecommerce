from django.contrib import admin
from . import models
# from .models import

"""
Pode se usar TabularInline ou StackedInline
"""


class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_produto',
                    'get_preco_formatado', 'get_preco_promocional_formatado', 'qualidade_equipamento', 'imagem']
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
