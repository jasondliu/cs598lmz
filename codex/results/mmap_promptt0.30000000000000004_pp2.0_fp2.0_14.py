import mmap
# Test mmap.mmap()
#
# This test is intended to be run from the root of the source tree.
#
# It tests mmap.mmap() by mapping a file and writing to it.
#
# See also test_mmap.py for a more comprehensive test.

import os
import unittest
from test import support
from test.support import TESTFN, unlink

class MmapTestCase(unittest.TestCase):
    def setUp(self):
        self.filename = TESTFN
        f = open(self.filename, 'w+')
        try:
            f.write('\0' * 1024)
        finally:
            f.close()

    def tearDown(self):
        unlink(self.filename)

    def test_basic(self):
        size = os.path.getsize(self.filename)
        f = open(self.filename, 'r+')
        try:
            m = mmap.mmap(f.fileno(), size)
        finally:
            f.close()
        self.assertEqual(len(m), size)
