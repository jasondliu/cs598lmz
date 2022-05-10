import mmap
# Test mmap.mmap() with more than 2GB data on 32-bit systems.
# This test is not run on 64-bit systems because it is irrelevant.

import os
import sys
import unittest
import mmap
from test import test_support

if sys.maxsize > 0x7FFFFFFF:
    raise unittest.SkipTest("This test is not relevant on 64-bit systems.")

# Get the size of the mmap module.  If it is less than 2GB, then this test is
# not relevant.
size = mmap.mmap.__sizeof__()
if size <= 0x7FFFFFFF:
    raise unittest.SkipTest("The mmap module size is less than 2GB.")

# Create a file of the right size.
filename = test_support.TESTFN
fp = open(filename, 'wb')
try:
    fp.seek(size - 1)
    fp.write('\0')
finally:
    fp.close()

# Check that mmap() works.
fp = open(filename, 'r+b')
