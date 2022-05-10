import select
import re
import time
import struct
from struct import unpack
from threading import Thread
from datetime import datetime
from os import listdir
from os.path import isfile, join
import sys
from ctypes import *
import os
from os import path

#initialize wifi module and set the baud rate
#os.system("sudo pigpiod")
#os.system("sudo pip install pigpio")
#os.system("sudo pip3 install pigpio")

mypath=path.dirname(path.realpath(__file__))

#os.system("sudo pigpiod -l")

#os.system("sudo pigpiod")

import pigpio

pi = pigpio.pi()

pi.set_mode(22,pigpio.OUTPUT)
pi.write(22,1)

if(len(sys.argv)>1):
	if(sys.argv[1]=="on"):
		pi.write(22,0)

#time.sleep(0.1)


