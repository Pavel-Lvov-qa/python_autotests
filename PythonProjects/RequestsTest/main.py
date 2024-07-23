import requests

Url = 'https://api.pokemonbattle.ru/v2'

Token ='c4f8a288f1fc19acdb5c787b17f04bd3'

Header = {'Content-Type' : 'application/json', 'trainer_token': Token}

body_registration = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_confirmacion = {
    "pokemon_id": "44644"
}

body_name={
    "pokemon_id": "44644",
    "name": "Буль",
    "photo_id": 2
}

'''response = requests.post(url = f'{Url}/pokemons', headers = Header, json = body_registration)
print(response.text)'''

'''response_confirmacion= requests.post(url=f'{Url}/trainers/add_pokeball', headers=Header, json = body_confirmacion)
print(response_confirmacion.text)'''

'''response_name = requests.put(url=f'{Url}/pokemons', headers=Header, json= body_name)
print(response_name.text)'''