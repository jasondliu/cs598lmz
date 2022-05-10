import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Documents/AzureIoTSuite/IoTEdgeSimulatedTemperatureSensor/app/db/temperature_db.db")
from time import sleep
from datetime import datetime

#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#GPIO.add_event_detect(11, GPIO.FALLING, callback=shutdown, bouncetime=300)

libc = ctypes.CDLL(ctypes.util.find_library('c'))

def shutdown(pin):
    libc.reboot(ctypes.c_int(0xfee1dead))

def get_temp():
    tempfile = open("/sys/bus/w1/devices/28-021564f9eaff/w1_slave")
    thetext = tempfile.read()
    tempfile.close()
    tempdata = thetext.split("\n")[1
