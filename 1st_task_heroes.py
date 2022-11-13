import requests

# Hulk_id = '332'
# Cap_id = '149'
# Thanos_id = '655'

class Superhero():
    def __init__(self, hero_id):
        self.base_url = 'https://akabab.github.io/superhero-api/api/'
        self.hero_id = hero_id

    def get_hero_itelligence(self):
        uri = f'powerstats/{self.hero_id}.json'
        request_url = self.base_url + uri 
        response = requests.get(request_url)
        int = response.json()['intelligence']
        return int
    
    def __lt__(self,other):
        return self.get_hero_itelligence() < other.get_hero_itelligence()

Hulk = Superhero('332')
Cap = Superhero('149')
Thanos = Superhero('655')

def who_cleverest():
    if (Hulk > Thanos) == True and (Hulk > Cap) == True:
        print('Халк самый умный!')
    elif (Cap > Thanos) == True and (Cap > Hulk) == True:
        print('Капитан Америка самый умный!')
    else:
        print('Танос самый умный')
    return
    

who_cleverest()