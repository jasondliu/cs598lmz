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
    print 'mmap: ', mm.readline()
    # read content via slice notation
    print 'mmap[:8]: ', mm[:8]
    # update content using slice notation;
    # note that new content must have same size
    mm[8:] = 'worldhello'
    mm.seek(0)
    print 'mmap: ', mm.readline()
    # close the map
    mm.close()
