import mmap
# Test mmap.mmap.read_byte
#
# This test is for the read_byte() method of mmap objects.
#
# read_byte() reads a single byte from the mmap object.
#
# This test does the following:
# 1. Creates an mmap object from a file
# 2. Reads a single byte from the mmap object
# 3. Checks the value of the byte read
# 4. Closes the mmap object
# 5. Closes the file
#
# This test is not intended to be exhaustive, but it is intended to
# catch common errors.
#
# This test was written by Tim Roberts, timr@probo.com
#

import sys
import mmap
import os

filename = "mmap_copy.txt"

# Create a file to be mmap'ed.

fp = open(filename, "w+")
fp.write("\0" * 1024)
fp.close()

# Create an mmap object from the file.

fp = open(filename, "r+")
