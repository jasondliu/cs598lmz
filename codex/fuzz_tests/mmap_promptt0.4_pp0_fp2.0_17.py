import mmap
# Test mmap.mmap()
#
# This test is derived from mmap_find.py, but uses mmap.mmap() instead
# of mmap.mmap().  mmap.mmap() is a wrapper around mmap.mmap() that
# takes care of the file descriptor for you.

import os
import mmap
import unittest

from test import test_support

class MmapTestCase(unittest.TestCase):
    def setUp(self):
        f = open(test_support.TESTFN, 'w+')
        try:
            f.write('\x00' * 1024)
            f.seek(0)
            self.m = mmap.mmap(f.fileno(), 1024)
        finally:
            f.close()

    def tearDown(self):
        self.m.close()
        os.unlink(test_support.TESTFN)

    def test_find(self):
        self.m[200:202] = 'xy'
        self.assertEqual(self.m.find('xy'), 200)
        self
