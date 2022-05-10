import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap documentation.

import os
import mmap

# Create a file and write a few lines to it
f = open('test.txt', 'w+')
f.write('Hello Python!\n')
f.write('Hello mmap!\n')
f.close()

# Open the file for reading
f = open('test.txt', 'r+')

# Create a mmap object
m = mmap.mmap(f.fileno(), 0)

# Read content via standard file methods
