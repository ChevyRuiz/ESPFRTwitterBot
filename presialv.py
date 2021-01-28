from twython import Twython
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

dalv = open(r"/home/pi/Desktop/txalvarito.txt","r+")
num_i = str(dalv.read())
num_i_len = str(len(num_i))
dalv.write("i")
textotw = ("---/// Desde que naci, han pasado " + num_i_len + " dias y Alvarito aún no es presidente ///---")
dalv.close()

message = textotw
twitter.update_status(status=message)
print("Tweeted: " + message)