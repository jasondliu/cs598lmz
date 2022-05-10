import mmap
# Test mmap.mmap()
#
# This test should be run with a command line argument that is the name of
# a file that is large enough to mmap.  For example, try:
#     python Lib/test/test_mmap.py /usr/dict/words

import unittest
import os
import mmap
import stat
import sys
import tempfile
import time
import struct
import array

from test import test_support

# Skip this test if the platform doesn't have a large enough file.
filename = test_support.findfile("mmap_largefile")
if not filename:
    raise unittest.SkipTest("cannot find a large enough file")

class MmapTests(unittest.TestCase):
    def setUp(self):
        f = open(filename, 'r+b')
        size = os.fstat(f.fileno())[stat.ST_SIZE]
        self.m = mmap.mmap(f.fileno(), size)
        f.close()

    def tearDown(self):
        self.m.close()

