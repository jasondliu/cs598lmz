import select
import sys
import textwrap
import time
import unittest

try:
    import Adafruit_GPIO.SPI as SPI
except (RuntimeError, ImportError):
    raise RuntimeError('This library requires the Adafruit_GPIO library\n'
                       'Install with: sudo pip install Adafruit_GPIO')

from PIL.ImageDraw import Draw
from PIL import Image, ImageDraw

try:
    # pylint: disable=wrong-import-position
    from . import Adafruit_GPIO as GPIO
except (ValueError, SystemError):
    # pylint: disable=import-error
    import Adafruit_GPIO as GPIO

# This is used during luma.oled install on Windows for packaging
try:
    import py_compile
except ImportError:
    pass


# pylint: disable=too-many-instance-attributes
class SSD1306Device(object):
    """Wrapper class around Adafruit_GPIO which represents the
       basic functionality of an SSD1306 device.
    """
    # pyl
