import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap module documentation.
#
# The test creates a file and writes some data to it.  It then mmaps the file
# and verifies that the data can be read back correctly.

import os
import mmap
import unittest

from test import test_support

# Create a file with some data in it
with open('mmaptest.dat', 'wb') as f:
    f.write('abcd\n')
    f.write('efgh\n')
    f.write('ijkl\n')

class MmapTests(unittest.TestCase):
    def setUp(self):
        # Open the file
        self.f = open('mmaptest.dat', 'r+b')

    def tearDown(self):
        self.f.close()
        os.unlink('mmaptest.dat')

    def test_read(self):
        # Simple read test
        m = mmap.mmap(self.f.fileno(), 0, access=mmap.ACCESS
