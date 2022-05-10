import threading
threading._DummyThread._Thread__stop = lambda x:42

from flask import Flask, request, abort, Response
from gpiozero import LED
import time

# setup
app = Flask(__name__)
led = LED(17)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/on')
def on():
    led.on()
    return 'ON'

@app.route('/off')
def off():
    led.off()
    return 'OFF'

@app.route('/blink')
def blink():
    led.blink(on_time=1, off_time=1, n=3)
    return 'BLINKING'

@app.route('/test')
def test():
    led.on()
    time.sleep(1)
    led.off()
    led.on()
    time.sleep(1)
    led.off()
    led.on()
