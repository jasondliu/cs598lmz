import mmap
import struct
import sys
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 16)

# Create a memory-map to the LCD display registers.  Note the
# configuration of the memory-mapped region.  We map the entire
# display-register address-range, but only the first 5 registers
# are actually used.
#
# The display is connected to the Raspberry Pi SPI0 bus, and has
# the following configuration:
#
#    - SPI Mode 0
#    - 8 bits per word
#    - MSB first
#    - Max speed of 1MHz
#
# The display is a 96x64 pixel monochrome display, and the
# display-registers are mapped as follows:
#
#    - Register 0: Display command/status
#    - Register 1: Column start address MSB (6 bits)
#    - Register 2: Column start address LSB (8 bits)
#
