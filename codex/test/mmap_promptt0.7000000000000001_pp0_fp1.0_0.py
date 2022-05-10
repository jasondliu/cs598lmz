import mmap
# Test mmap.mmap
import mmap

from mmap import PAGESIZE, ALLOCATIONGRANULARITY
from mmap import ACCESS_READ, ACCESS_WRITE, ACCESS_COPY
from mmap import MAP_ANON, MAP_PRIVATE, MAP_SHARED

from mmap import error as mmap_error
from mmap import mmap as _mmap
from stat import ST_MODE

from test import support

MMAP_SIZE = support.findfile("mmap_small.txt", subdir="mmap")
MMAP_REGULAR = support.findfile("mmap_regular.txt", subdir="mmap")
MMAP_SMALL = support.findfile("mmap_small.txt", subdir="mmap")
MMAP_COPY = support.findfile("mmap_copy.txt", subdir="mmap")
MMAP_BINARY = support.findfile("mmap_binary.bin", subdir="mmap")

# Check mmap module constants
PAGELEN = PAGESIZE
