import requests
import pytest

Url = 'https://api.pokemonbattle.ru/v2'

Token ='c4f8a288f1fc19acdb5c787b17f04bd3'

Header = {'Content-Type' : 'application/json', 'trainer_token': Token}

Trainer_id= '4629'

def test_status_code():
    response=requests.get(url=f'{Url}/trainers',params={'trainer_id': Trainer_id})
    assert response.status_code == 200