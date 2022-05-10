import ctypes
import ctypes.util
import threading
import sqlite3
import time
import html2text
from flask import Flask, render_template, session



## setup GPIO ports
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# LEDS
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

# button
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#LCD ports
GPIO.setup(8, GPIO.OUT) 
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO
