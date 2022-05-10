import threading
threading.stack_size(67108864)

# Import the libraries
import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

# Set the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
redPin = 18
greenPin = 23
bluePin = 24
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

# Set the GPIO pins for PWM
red = GPIO.PWM(redPin, 500)
red.start(100)
green = GPIO.PWM(greenPin, 500)
green.start(100)
blue = GPIO.PWM(bluePin, 500)
blue.start(100)

# Set the bot token
bot = telepot.Bot('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Define the colors
def redOn():
    red.ChangeDutyCycle(100)

