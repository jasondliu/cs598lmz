import mmap
# Test mmap.mmap()
#
# Test mmap module (mmap.mmap())
# Create a file that can be memory-mapped.
#
# Note: This example requires Python 2.0 or later.

# from mmap import mmap,ACCESS_READ
from mmap import *
import os

# Create a file and write some data to it

f = open(os.tmpnam(), 'w+')
f.write('Hello Python!')
f.close()

# Open the file again, in read-only binary mode
f = open(os.tmpnam(), 'r+b')

# Create a memory-map to the file, size 0 means whole file
m = mmap(f.fileno(), 0)
