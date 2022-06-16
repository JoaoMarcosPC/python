import requests

baseURL = 'https://pokeapi.co/api/v2/'
endpoint = 'pokemon'
pkmID = '3'

def main_request(baseurl, endpoint):
    r = requests.get(baseurl + endpoint)
    return r.json()

def print_pkm_info(response):
    print(response['name'])
    print(response['types'])
    return

data = main_request(baseURL, endpoint + '/' + pkmID)

print_pkm_info(data)
