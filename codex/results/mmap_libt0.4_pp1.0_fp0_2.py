import mmap
import struct
import os
import time
import sys
import numpy as np
import matplotlib.pyplot as plt

# Open the device file
fd = os.open("/dev/uio0", os.O_RDWR)

# mmap the device into memory
m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0)

# Create a numpy array backed by the memory map
nparray = np.frombuffer(m, dtype=np.uint32)

# Read the value of the counter
print(nparray[0])

# Write a new value to the counter
nparray[0] = 0

# Read the value of the counter again
print(nparray[0])

# Unmap the memory
m.close()

# Close the device file
os.close(fd)
