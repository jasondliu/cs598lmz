import mmap
import os
import sys
import time

# This is a simple script to read the contents of a file and write them to a
# device.

# The file is read in chunks of 4K.

# The device is opened with mmap.

# The mmap is a memory map of the device.

# The file is read in chunks of 4K and the mmap is written to.

# The mmap is flushed to the device.

# The mmap is then closed.

# The file is closed.

# The device is closed.

# The script exits.

# The script takes two arguments:

# The first is the name of the file to read.

# The second is the name of the device to write to.

# The script is called like this:

# python3 write_file_to_device.py <file> <device>

# The script is called like this:

# python3 write_file_to_device.py /home/pi/Desktop/test.txt /dev/sda1

# The script is called like this:

