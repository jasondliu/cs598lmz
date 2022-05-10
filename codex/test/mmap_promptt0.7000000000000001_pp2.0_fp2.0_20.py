import mmap
# Test mmap.mmap(-1, length, prot, flags, fd, offset)
from mmap import mmap, PROT_READ, MAP_SHARED, MAP_FIXED, ACCESS_READ, ALLOCATIONGRANULARITY
import os
import sys
from test import support

PAGESIZE = mmap.PAGESIZE

if hasattr(os, 'O_BINARY'):
    O_BINARY = os.O_BINARY
else:
    O_BINARY = 0

