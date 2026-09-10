# Uvod v API - je
import requests #pip install requests

base_url = "https://api.chucknorris.io/jokes/random"

call = requests.get(base_url)
#print(call.text) preverimo vesbino klica

callJSON = call.json()
#print(callJSON)
print(callJSON["value"])