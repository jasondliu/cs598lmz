import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from gpiozero import LED
from gpiozero import Button

from time import sleep
from time import time

from signal import pause

from random import randint

from os import listdir
from os.path import isfile, join

from subprocess import call

import pygame

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO Pins
GPIO.setup(17, GPIO.IN) # Left
GPIO.setup(27, GPIO.IN) # Right
GPIO.setup(22, GPIO.IN) # Up
GPIO.setup(23, GPIO.IN) # Down
GPIO.setup(24, GPIO.IN) # A
GPIO.setup(25, GPIO.IN) # B
GPIO.setup(5, GPIO.IN) # X
GPIO.setup(6, GPIO.IN) # Y
