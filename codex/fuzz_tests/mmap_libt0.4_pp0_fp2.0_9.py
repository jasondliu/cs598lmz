import mmap
import sys
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

from Adafruit_MPR121 import MPR121

# Raspberry Pi configuration.
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000))

# Initialize display.
disp.begin()

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize MPR121 using default address (0x5A).  On the MPR121 breakout,
# this is the only address possible so we pass in the value here which is
# ignored by the library.
if not cap.
