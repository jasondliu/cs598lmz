import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

from time import sleep
from random import randint
from itertools import cycle

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero.tools import random_values

from signal import pause

factory = PiGPIOFactory(host='192.168.1.4')

led = LED(17, pin_factory=factory)

for i in range(10):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)
