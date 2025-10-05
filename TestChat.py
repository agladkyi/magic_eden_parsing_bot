import requests

TOKEN = ''
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response = requests.get(url)
data = response.json()

print(response)