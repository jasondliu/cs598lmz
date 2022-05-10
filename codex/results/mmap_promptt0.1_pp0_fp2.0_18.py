import mmap
# Test mmap.mmap()
#
# This test is derived from the test case for mmap.mmap() in the Python
# standard library.
#
# The test case is modified to use the mmap.mmap() function in the
# mmap module.

import os
import sys
import unittest
import mmap

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = os.path.join(os.path.dirname(__file__), 'mmaptest.dat')
        f = open(self.filename, 'w+b')
        try:
            f.write(b'\0' * mmap.ALLOCATIONGRANULARITY)
        finally:
            f.close()

    def tearDown(self):
        os.unlink(self.filename)

    def test_basic(self):
        size = 200
        f = open(self.filename, 'r+b')
        try:
            m = mmap.mmap(f.fileno(), size)
        finally:
            f.close()
