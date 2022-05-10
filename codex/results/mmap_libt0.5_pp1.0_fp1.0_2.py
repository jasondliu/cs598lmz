import mmap
import struct
import sys
import os

# open the file
f = open("/dev/mem", "r+b")

# memory-map the file, size 0 means whole file
map = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0x43C00000)

# read content via standard file methods
print "Current content:", repr(map.read(1))

# read/write a single byte via slice notation
map[0] = '\x00'

# write a byte sequence
map[1:5] = '\x00\x01\x02\x03'

# update file with modified buffer
map.flush()

# close the map
map.close()

# close the file
f.close()
