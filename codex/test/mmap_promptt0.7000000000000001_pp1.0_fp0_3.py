import mmap
# Test mmap.mmap(0,1024) on unix
#
# Author: Zoran Isailovski, zoran at isailovski.com
#

# This script writes the string "hello" five times to a memory mapped file.
# Then it reads the string back and prints it.

# The memory mapped file contents after this script executes are:
# hellohellohellohellohello

import mmap

with open('mmapfile', 'r+') as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
