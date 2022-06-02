from django.contrib import admin
from turismo.models import Restaurante,Hotel,Atrativo,Evento

class Restaurantes(admin.ModelAdmin):
    list_display = ('id','nome','url') # mostrar os campos do model
    list_display_links = ('id','nome','url') #link para acessar o atributo do model
    search_fields = ('nome',) # campo para realizar pesquisa
class Hoteis(admin.ModelAdmin):
    list_display = ('id','nome','url')
    list_display_links = ('id','nome','url')
    search_fields = ('nome',)

class Atrativos(admin.ModelAdmin):
    list_display = ('id','nome','descricao')
    list_display_links = ('id','nome',)
    search_fields = ('nome',)
class Eventos(admin.ModelAdmin):
    list_display = ('id','nome','local','descricao')
    list_display_links = ('id','nome',)
    search_fields = ('nome',)


admin.site.register(Restaurante,Restaurantes) # permite criar uma instancia de Restaurante
admin.site.register(Hotel,Hoteis)
admin.site.register(Atrativo,Atrativos)
admin.site.register(Evento,Eventos)
