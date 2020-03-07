from django.contrib import admin
from .models import Noticia,Pessoa,Tag,Comentario,Categoria

@admin.register(Noticia,Pessoa,Tag,Categoria,Comentario)
class NoticiaAdmin(admin.ModelAdmin):
    pass