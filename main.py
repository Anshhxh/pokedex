import requests

def get_pokemon(name):

    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"

    try:
        response = requests.get(url,timeout = 10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError:
        print("Pokemon not found! Please check the name.")
        return None

    except requests.exceptions.RequestException:
        print("Network Error. Please try again later.")
        return None


def display_pokemon(data):

    print("\n========== POKEDEX ==========")

    print("Name:", data["name"].capitalize())
    print("ID:", data["id"])
    print("Height:", data["height"] / 10, "m")
    print("Weight:", data["weight"] / 10, "kg")

    print("\nTypes:")

    for item in data["types"]:
        print("-", item["type"]["name"])

    print("\nAbilities:")

    for item in data["abilities"]:
        ability_name = item["ability"]["name"]
        hidden = item["is_hidden"]

        if hidden:
            print(f"- {ability_name} (Hidden Ability)")

        else:
            print(f"- {ability_name}")

    image_url = data["sprites"]["other"]["official-artwork"]["front_default"]

    if image_url:
        print("Artwork URL: ", image_url)
    else:
        print("Artwork Unavailable!")

    print("\nStats:")
    for item in data["stats"]:
        print(f"- {item['stat']['name']}: {item['base_stat']}")

    print("=============================")


print("\nWelcome to Pokedex!")

while True:
    pokemon_name = input("Enter pokemon name: ")

    data = get_pokemon(pokemon_name)

    if data:
        display_pokemon(data)

    while True:
        choice = input("\nSearch another Pokemon? (yes/no):").lower().strip()
        if choice == "no":
            print("Thankyou for using Pokedex!")
            exit()

        elif choice == "yes":
            break

        else:
            print("Invalid Choice! Please enter yes or no.")
