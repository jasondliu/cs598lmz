import mmap
# Test mmap.mmap
import os

# Open file for reading
fd = os.open('data', os.O_RDWR)

# Create mmap object
m = mmap.mmap(fd, 0)

# Read from file
