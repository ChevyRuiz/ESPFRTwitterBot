from twython import Twython
from randomwordfr import RandomWordFr
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


rw = RandomWordFr()
palabra = str(rw)
lpalabra = str(len(palabra))
numlpalabra = len(palabra)
while (numlpalabra > 280 ):
   rw = RandomWordFr()
   palabra = str(rw)
   lpalabra = str(len(palabra))
   numlpalabra = len(palabra)
   
message = palabra
twitter.update_status(status=message)
print("Tweeted: " + message)