import pyjokes
from twython import Twython
from bs4 import BeautifulSoup
import requests
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def get_random_chiste():
    response = requests.get('http://www.chistes.com/ChisteAlAzar.asp?n=3')
    soup = BeautifulSoup(response.text, "html.parser")
    chiste = soup.find("div", "chiste").text
    
    return chiste

chiste = (get_random_chiste())
lchiste = len(chiste)

while (lchiste > 280):
    chiste = (get_random_chiste())
    lchiste = len(chiste)

print(chiste)
print(lchiste)
message = chiste
twitter.update_status(status=message)
print("Tweeted: " + message)
