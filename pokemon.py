import requests

def get_pokemon(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"

    try:
        response = requests.get(url,timeout = 10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError:
        return None

    except requests.exceptions.RequestException:
        return None

    
def get_pokemon_list(limit=12, offset=0):

    url = "https://pokeapi.co/api/v2/pokemon"

    try:
        response = requests.get(
            url,
            params={
                "limit": limit,
                "offset": offset
            },
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException:
        return None



def get_pokemon_by_type(type_name):

    url = f"https://pokeapi.co/api/v2/type/{type_name.lower()}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException:
        return None
