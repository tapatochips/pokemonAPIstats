#i import both random and requests, random will make more sense in a second lol
import random
import requests

#connect to the api and set the limit to 1015 pokemon, at the time of making this, according to google there are 1015 different pokemon
pokemon_list_url = 'https://pokeapi.co/api/v2/pokemon/?limit=1015'
pokemon_list_response = requests.get(pokemon_list_url)
if pokemon_list_response.status_code != 200:
    print(f"Failed to get Pokemon list. Status code: {pokemon_list_response.status_code}")
    exit()

pokemon_list = pokemon_list_response.json()['results']

#here i select 5 random pokemon
random_pokemon = random.sample(pokemon_list, 5)

#loop over the pokemon
for pokemon in random_pokemon:
    pokemon_url = pokemon['url']
    pokemon_response = requests.get(pokemon_url)
    if pokemon_response.status_code != 200:
        print(f"Failed to get Pokemon info. Status code: {pokemon_response.status_code}")
        continue

    pokemon_info = pokemon_response.json()

    #here i extract the desired info about the pokemon, i also included type because it is important to know the pokemons types
    name = pokemon_info['name']
    hp = pokemon_info['stats'][0]['base_stat']
    attack = pokemon_info['stats'][1]['base_stat']
    defense = pokemon_info['stats'][2]['base_stat']
    ability_name = pokemon_info['abilities'][0]['ability']['name']
    base_experience = pokemon_info['base_experience']
    sprite_url = pokemon_info['sprites']['front_shiny']
    types = ", ".join([t['type']['name'] for t in pokemon_info['types']])
  


    #i print the info on each pokemon
    print(f"Name: {name}")
    print(f"HP: {hp}")
    print(f"Attack: {attack}")
    print(f"Defense: {defense}")
    print(f"Ability: {ability_name}")
    print(f"Base Experience: {base_experience}")
    print(f"Front Shiny Sprite URL: {sprite_url}")
    print(f"Types: {types}")
    print("--------------------------------------------")
