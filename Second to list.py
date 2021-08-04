print(" Please enter seconds you want to convert")
from math import *

second= int(input())

hour=floor(second/3600)

minute = floor((second%3600)/60)

sec= (floor(second%3600)%60)

print(hour,":",minute,":",sec)