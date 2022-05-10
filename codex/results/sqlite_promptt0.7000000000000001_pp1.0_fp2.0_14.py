import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/Desktop/temps.db")
import datetime
import time
from time import sleep
from datetime import datetime
import Adafruit_DHT
from gpiozero import LED

# Setup LED
blue = LED(18)
red = LED(23)
yellow = LED(24)
green = LED(25)

# Create a global object that will be used to communicate between threads
global comm
comm = threading.Event()
# Set the event to false
comm.clear()
# Create a global variable to store the value to send
global value
value = 0

# Initialize the OLED display using GPIO pins
# NOTE: The width and height are different for the smaller 128x64 OLEDs
#dht_sensor = Adafruit_DHT.DHT11
dht_sensor = Adafruit_DHT.DHT22
dht_pin = 4

# Set the OLED width and height
disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=0, gpio=
