import mmap
# Test mmap.mmap
mmap.mmap

Testing
"""

import mmap
import unittest

from test import support

DEFAULT_SIZE = 1024

PAGESIZE = mmap.PAGESIZE
if PAGESIZE > 2048:
    # Some systems have a very large PAGESIZE and an equally large
    # ALLOCATIONGRANULARITY.  That makes mmap() allocations very expensive,
    # which makes running the tests very slow.  If we detect that, use a
    # smaller size.
    PAGESIZE = 2048

# windows 1999 and earlier can't handle more than 256 mappings of a file
# at one time, so we have to make do with a smaller number of repetitions
# in that case.
import sys
if not hasattr(sys, 'getwindowsversion') or sys.getwindowsversion() < (4, 0, 0, 0, ''):
    REPETITIONS = 5
    MAX_FD_COUNT = 50
else:
    REPETITIONS = 50
    MAX_FD_COUNT = 250


def make_empty_file(num_chars):
