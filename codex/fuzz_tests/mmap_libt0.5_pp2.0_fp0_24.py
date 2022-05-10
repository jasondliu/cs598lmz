import mmap
import sys
import time
from datetime import datetime
import os

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x71)

# Initialize the display. Must be called once before using the display.
segment.begin()

print("Press CTRL+Z to exit")

# Continually update the time on a 4 char, 7-segment display
while(True):
  now = datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second

  segment.clear()
  # Set hours
  segment.set_digit(0, int(hour / 10))     # Tens
  segment.set_digit(1, hour % 10)          # Ones
  # Set minutes
  segment.set_digit(2, int(minute / 10))   # Tens
  segment.set_digit(3, minute %
