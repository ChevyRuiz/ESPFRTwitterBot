from twython import Twython
from gpiozero import CPUTemperature
import datetime
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

date = datetime.datetime.now()
date_int = int (date.hour)
cpu = CPUTemperature()
twdate = str(datetime.datetime.now())
twcpu = str(cpu.temperature)

print (date.hour)

print (date_int)

textdt = ("")

if date_int > 5 and date_int < 12 :

    textdt = ("Buenos Dias! el tiempo es: ")

   
elif date_int > 12 and date_int < 20:
    
    textdt = ("Buenas tardes, el tiempo es: ")
  
else:
    textdt = ("Buenas noches, el tiempo es: ")
    
    
complete_message = (textdt + twdate + "  /  " + "La temperatura de mi CPU es: " + twcpu + "C")
message = complete_message
twitter.update_status(status=message)
print("Tweeted: " + message)