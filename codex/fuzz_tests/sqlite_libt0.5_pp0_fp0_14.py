import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import logging
import logging.handlers
import json

# Open the database
db = sqlite3.connect('/home/pi/Documents/DoorPi/door_log.db')
cursor = db.cursor()

# Set up logging
LOG_FILENAME = "/home/pi/Documents/DoorPi/door_log.log"
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=5000000, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set up the RF
