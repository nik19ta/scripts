import json
import requests
from sh import mv, git, mkdir

username = input('Имя пользователя: ')

response = requests.get(f'https://api.github.com/users/{username}/repos')

json_response = response.json()
print(f'Началось кланирование репозиториев {username}')
mkdir(username)
for i in json_response:
    git("clone", i['html_url'])
    print(f"{i['name']} склонирован в папку ./{username}")
    mv(i['name'], f"./{username}")
