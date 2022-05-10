import socket
import time
import random
import spidev
import neopixel

HOST = ''
PORT = 5000
SOCKET_LIST = []
RECV_BUFFER = 4096

# Number of NeoPixels
PIXEL_COUNT = 144
EVENT_KEY_fwd = 255

# For NeoPixels
LED_PIN = 18  # Current GPIO pin connected to the pixels.
ORDER = neopixel.GRB

# For SPI
spi = spidev.SpiDev()
spi.open(0, 0)

# Create NeoPixel object with appropriate configuration.
strip = neopixel.NeoPixel(LED_PIN, PIXEL_COUNT)


def neoPixelColorWipe(strip, color):
    """Wipe color across strip a pixel at a time."""
    for i in range(strip.count()):
        strip[i] = color
        strip.write()


def neoPixelWheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return neopixel.Color(
