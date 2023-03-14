import requests


class Superhero:
    def __init__(self):
        pass

    def get_superhero(self):
        url = "https://akabab.github.io/superhero-api/api"
        final_part = "/all.json"
        final_url = url + final_part
        response = requests.get(final_url)
        data = response.json()

        max_intelligence = 0
        hero_name = ''
        for hero in data:
            if hero['name'] in ['Hulk', 'Captain America', 'Thanos'] and \
                    hero['powerstats']['intelligence'] > max_intelligence:
                max_intelligence = hero['powerstats']['intelligence']
                hero_name = hero['name']
        return hero_name


hero = Superhero()
print(f"Максимальный уровень интеллекта у: {hero.get_superhero()}.")
