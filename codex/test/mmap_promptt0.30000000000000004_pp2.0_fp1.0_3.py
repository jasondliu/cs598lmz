import mmap
# Test mmap.mmap()
#
# This is a test of the mmap.mmap() function.
#
# This test creates a file, writes some data to it, mmaps it, and then
# verifies that the data is correct.

import os
import mmap
import unittest

from test.support import TESTFN, unlink

class MmapTests(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_basic(self):
        # Create a file and write some data to it
        self.f.write(b"\x00\x01\x02\x03\x04\x05\x06\x07")
        self.f.flush()

        # Map the file into memory
        m = mmap.mmap(self.f.fileno(), 8)

        # Check that the mapping worked
