from re import search
from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria')

    # add links
    list_display_links = ('id', 'nome', 'sobrenome')
    # add filtros
    # list_filter = ('nome', 'sobrenome')
    list_per_page = 5 # coloca 10 elementos por página
    search_fields = ('nome', 'sobrenome') # cria um campo de busca por nome e sobrenome

# registrando modelo categoria no site
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)