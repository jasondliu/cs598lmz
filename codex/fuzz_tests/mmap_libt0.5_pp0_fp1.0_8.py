import mmap
import struct
import sys
import time

from PIL import Image

import RPi.GPIO as GPIO

# This is the memory location of the frame buffer.
# It changes between revisions of the Raspberry Pi.
# Check /proc/cmdline for the location of fb0
# You can also run the command 'cat /proc/fb'
# to get the frame buffer location.
FB_MEM_LOCATION = 0x00040000

# This is the size of the frame buffer.
# It changes between revisions of the Raspberry Pi.
FB_MEM_SIZE =  0x0009b000

# This is the memory location of the GPIO registers.
# It changes between revisions of the Raspberry Pi.
# Check /proc/iomem for the location of GPIO
# You can also run the command 'cat /proc/iomem'
# to get the GPIO location.
GPIO_BASE_LOCATION = 0x20200000

# This is the size of the GPIO registers.
# It changes between revisions of the Raspberry Pi.
GPIO_MEM_SIZE = 0x28

# This
