import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_READ)
# Test mmap.mmap(fileno, length, access=ACCESS_WRITE)
# Test mmap.mmap(fileno, length, access=ACCESS_COPY)
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT)

import os
import unittest
from test import test_support

try:
    mmap.ACCESS_READ
except AttributeError:
    raise unittest.SkipTest("mmap.ACCESS_* not defined")

# Test that the access argument is accepted

# A file that is large enough to mmap
FILESIZE = 1024 * 1024

# The size of the mapping
MAPSIZE = 1024

class MmapTests(unittest.TestCase):

    def setUp(self):
        # Create a file to be mapped
        f = open(test_support.TESTFN, 'wb+')
