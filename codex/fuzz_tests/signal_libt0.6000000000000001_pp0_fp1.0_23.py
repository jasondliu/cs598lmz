import signal
signal.signal(signal.SIGINT, signal_handler)

# check if we have a config file
if not os.path.isfile('config.py'):
    print("config.py not found.")
    print("Please copy config.default.py to config.py and customize it.")
    sys.exit(1)

# import config
import config

# import modules
import sys
import json
import time
import math
import threading
import subprocess
import re
import argparse

import psutil

from datetime import datetime, timedelta
import dateutil.parser

import requests
import feedparser

# import modules from local dir
sys.path.append(os.getcwd())
import LCD
import LCD.HD44780
import LCD.I2C
import LCD.PCF8574
import LCD.PCF8574.GPIO
import LCD.PCF8574.BitBang
import LCD.PCF8574.CharLCD

# define functions
def get_cpu_temperature():
    process = subprocess.Popen(['/opt/
