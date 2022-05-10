import select
import socket
import sys
import time
import sys
import time

from serial import Serial
from serial.tools import list_ports

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont
import RPi.GPIO as GPIO

# Initialize the I2C bus.
serial = i2c(port=1, address=0x3C)

# Initialize the display.
device = ssd1306(serial, rotate=0)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN)

# Initialize the font
font = ImageFont.truetype("./fonts/FreeMono.ttf", 10)

# Initialize the serial port
ser = Serial(
    port="/dev/ttyUSB0", baudrate=115200, bytesize=8, parity="N", stopbits=1
)

