# coding=utf-8
import requests
from django.shortcuts import render, redirect
#LISTAR

def listar_pokemon(request):
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=9'
    offset = 0
    next = 1
    previus = -1

    if 'next' in request.GET:
        previus = int(request.GET.get('next'))-1
        next = int (request.GET.get('next'))+1
        offset = int(request.GET.get('next'))*9

    if 'previus' in request.GET:
        previus = int(request.GET.get('previus'))-1
        offset = int(request.GET.get('previus'))*9

    args = {'offset':offset} if offset else {}
    response = requests.get(url, params=args)
    if response.status_code == 200:
        payload = response.json()
        result = payload.get('results', [])
        if result:
            pokemonS = []
            for pokemon in result:
                nombre = pokemon['name']
                response = requests.get(pokemon['url'])
                if response.status_code == 200:
                    payload = response.json()
                    pokemon_id = payload.get('id', [])
                    img = payload.get('sprites', [])
                    imagen = img['other']
                    dir = {'nombre': nombre, 'id': pokemon_id, 'imagen': imagen}
                    pokemonS.append(dir)
    return render(request, 'templates/listar_pokemon.html', {'pokemonS':pokemonS, 'next':next, 'previus':previus})

def tipo(request, id_tipo):
    id = id_tipo
    url = 'https://pokeapi.co/api/v2/type/'+str(id)
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        pokemon_id = payload.get('id', [])
        pokemon_name = payload.get('pokemon', [])
        tipo_name = payload.get('name')
        pokemonS = []
        for pokemon in pokemon_name:
                links = pokemon['pokemon']
                response = requests.get(links['url'])
                if response.status_code == 200:
                    payload = response.json()
                    pokemon_id = payload.get('id', [])
                    nombre = payload.get('name', [])
                    img = payload.get('sprites', [])
                    imagen = img['other']
                    dir = {'id': pokemon_id, 'imagen': imagen, 'nombre':nombre}
                    pokemonS.append(dir)
    return render(request, 'templates/base/pokemon_tipo.html', {'pokemonS':pokemonS, 'tipo_name':tipo_name})


def getInfoPokemon(request, id_pokemon):
    id = id_pokemon
    url = 'https://pokeapi.co/api/v2/pokemon/'+str(id)
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        nombre = payload.get('name', [])
        img = payload.get('sprites', [])
        imagen = img['other']
        peso = payload.get('weight', [])
        altura = payload.get('height', [])
        habilidad = payload.get('abilities', [])
        tipo = payload.get('types', [])
        movimiento = payload.get('moves', [])

        if tipo:
            pokemonS = []
            for pokemon in tipo:
                pokemonUrl = pokemon['type']
                response = requests.get(pokemonUrl['url'])
                if response.status_code == 200:
                    payload = response.json()
                    id_tipo = payload.get('id', [])
                    nombre_tipo = payload.get('name', [])
                    dir = {'id':id_tipo, 'nombre':nombre_tipo}
                    pokemonS.append(dir)

        diccionario = {'nombre':nombre, 'imagen':imagen, 'peso':peso, 'altura':altura}

    return render(request, 'templates/pokemon_info.html', {'pokemon':diccionario, 'habilidad':habilidad, 'tipo':tipo, 'movimiento':movimiento, 'pokemonUrl':id_tipo, 'pokemonS':pokemonS})

def tiposPokemon(request):
    url = 'https://pokeapi.co/api/v2/type/'
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        result = payload.get('results', [])
        if result:
            pokemonS = []
            for pokemon in result:
                nombre = pokemon['name']
                response = requests.get(pokemon['url'])
                if response.status_code == 200:
                    payload = response.json()
                    id = payload.get('id', [])
                    tipo = pokemon.get('name', [])
                    dir = {'tipo': tipo, 'id':id}
                    pokemonS.append(dir)

    return render(request, 'templates/select_tipo.html', {'id':id, 'pokemonS':pokemonS})