import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'd38dc93f00fbdfa8b617308a95369805'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_pokemon_creation = {
    "name": "generate",
    "photo_id": -1
}

body_change_pokemon = {
    "pokemon_id": '287197',
    "name": "Lok Rok",
    "photo_id": '115'
}

body_catch_pokemon_in_pokeball ={
    'pokemon_id': '287194'
}


'''Создание покемона'''
    
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_creation)
print (response_create.text)
print (response_create.status_code)

message = response_create.json()['message']
print(message)

'''pokemon_id = response_create.json()['id']
print(pokemon_id)'''


'''Изменить покемона'''

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_pokemon)
print (response_change.text)
print (response_change.status_code)

message = response_change.json()['message']
print(message)


'''Поймать покемона в покебол'''

response_catch_pokemon_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon_in_pokeball)
print (response_catch_pokemon_in_pokeball.text)
print (response_catch_pokemon_in_pokeball.status_code)

message = response_catch_pokemon_in_pokeball.json()['message']
print(message)