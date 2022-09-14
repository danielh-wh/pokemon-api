from os import path

from django.conf.urls import url
from app.pokemones.views import listar_pokemon, getInfoPokemon, tipo, tiposPokemon

urlpatterns = [
    url(r'^$', listar_pokemon, name='listar_pokemon'),
    url(r'^informacion_pokemon/(?P<id_pokemon>\d+)/$', getInfoPokemon, name='informacion_pokemon'),
    url(r'^tipo/(?P<id_tipo>\d+)/$', tipo, name='tipo'),
    url(r'^tipos_pokemon/$', tiposPokemon, name='tipos_pokemon'),
]