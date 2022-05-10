import mmap
# Test mmap.mmap()
#
# This test is derived from test_mmap.py in the Python standard library,
# but uses a larger file.

import os
import unittest
import mmap

from test.support import TESTFN, unlink, unlink

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = TESTFN
        f = open(self.filename, 'wb+')
        try:
            # bss will be zeroed out by mmap
            f.write(b'\0' * mmap.ALLOCATIONGRANULARITY)
        finally:
            f.close()

    def tearDown(self):
        unlink(self.filename)

    def test_bad_args(self):
        # Try creating with various combinations of bad arguments
        self.assertRaises(TypeError, mmap.mmap, 1, 2, 3, 4, 5)
        self.assertRaises(TypeError, mmap.mmap, 1, 2, 3, 4)
