import socket
import time
from multiprocessing import Process

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106

# -----------------------------------------------------------------------------
# Global Variables
# -----------------------------------------------------------------------------
# Set to True if using the Adafruit 128x32 OLED breakout
is_128x32 = False

# Set to True if using the Adafruit 128x64 OLED breakout
is_128x64 = True

# -----------------------------------------------------------------------------
# Display Initialization
# -----------------------------------------------------------------------------
# Raspberry Pi pin configuration:
RST = None

# 128x32 display with hardware I2C:
if is_128x32:
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0
