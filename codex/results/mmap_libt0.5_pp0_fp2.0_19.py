import mmap
import os
import sys
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageOps

from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Configuration
# ===========================================================================

# This is the offset in seconds to add to the internal clock to correct for
# your timezone.  For Eastern Standard Time in the USA, this would be -5.
# For Greenwich Mean Time, this would be zero.  Feel free to tweak to match
# your locale as needed.
timezone_offset = 0

# This is the width and height of the display in pixels.
display_width = 128
display_height = 64

# This is the padding to use around the display image in pixels.
padding = 2

# This is the font file to load.  Make sure it's a .pil file, not a .pbm file!
# If you don't have a .pil file, you can convert one from a .pbm file using:
#
#     pilfont myfont.pbm myfont.
