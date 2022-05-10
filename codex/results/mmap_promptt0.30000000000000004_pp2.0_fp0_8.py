import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0)
#
# This test is based on the mmap module test.

import os, sys
import unittest
from test import test_support

import mmap

# We can't use support.TESTFN because mmap.mmap needs a real file
# on the current system.
filename = test_support.TESTFN

class MmapTests(unittest.TestCase):
    def setUp(self):
        fp = open(filename, 'w+')
        try:
            fp.write('\0' * mmap.ALLOCATIONGRANULARITY)
        finally:
            fp.close()

    def tearDown(self):
        os.unlink(filename)

    def test_bad_args(self):
        # Try a bunch of invalid calls to mmap.mmap() to
        # exercise the checks for invalid arguments.
        fp = open(filename, 'r+')
        self.assertRaises(TypeError, mmap.mmap, 1)
