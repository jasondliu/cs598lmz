import mmap
import struct
import sys
import time

from PIL import Image

# Open the device in read-only mode.
fd = os.open("/dev/fb0", os.O_RDONLY)

# Memory-map the device; size 0 means to map the whole thing.
buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)

# Get the fixed screen info.
finfo = fcntl.ioctl(fd, termios.FBIOGET_FSCREENINFO, struct.pack('256s', ''))

# Get the variable screen info.
vinfo = fcntl.ioctl(fd, termios.FBIOGET_VSCREENINFO, struct.pack('256s', ''))

# Get the size of the screen in bytes.
screensize = vinfo.fetch('yres_virtual') * finfo.fetch('line_length')

# Create an image-object in PIL to store the screenshot.
image = Image.new('RGB', (vinfo.
