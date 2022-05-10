import mmap
# Test mmap.mmap()
#
# This test is based on the example in the mmap module documentation.
# It is not a complete test, but it does exercise the code.

import os
import mmap
import unittest

from test import test_support

filename = test_support.TESTFN

class MmapTests(unittest.TestCase):
    def setUp(self):
        f = open(filename, 'w+')
        try:
            # We need a file with some data for this test to work
            f.write('\x00' * 1024)
        finally:
            f.close()

    def tearDown(self):
        os.unlink(filename)

    def test_basic(self):
        size = 1024
        f = open(filename, 'r+')
        try:
            m = mmap.mmap(f.fileno(), size)
        finally:
            f.close()
        self.assertEqual(len(m), size)
        self.assertEqual(m[0], '\x00')
        self.assertE
