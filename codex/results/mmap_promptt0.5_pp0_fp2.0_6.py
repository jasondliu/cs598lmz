import mmap
# Test mmap.mmap(fileno, size)
#
# This is a test case for http://bugs.python.org/issue1726759
#
# Ensure that mmap.mmap(fileno, size) works, even if the file is
# smaller than the specified size.

import os
import sys
import unittest
from test import test_support

def _create_file(fn, size):
    with open(fn, 'wb') as f:
        f.write('\0' * size)

class TestMmapFile(unittest.TestCase):
    def setUp(self):
        self.filename = test_support.TESTFN
        _create_file(self.filename, 4096)
        self.f = open(self.filename, 'rb+')

    def tearDown(self):
        self.f.close()
        os.remove(self.filename)

    def test_mmap_smaller_file(self):
        m = mmap.mmap(self.f.fileno(), 4096)
        m[:] = 'a' * 4096
        m
