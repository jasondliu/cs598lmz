import mmap
# Test mmap.mmap()
#
# This test is not very thorough.  It just makes sure that mmap.mmap()
# can create a read-write anonymous mapping, and that a few simple
# operations work.

import mmap
import os
import unittest
from test import support

class MmapTests(unittest.TestCase):

    def test_anonymous(self):
        # Test anonymous mappings.
        size = 1024
        with mmap.mmap(-1, size) as m:
            self.assertEqual(len(m), size)
            self.assertEqual(m.read(1), b'\x00')
            m.write(b'a')
            m.seek(0)
            self.assertEqual(m.read(1), b'a')
            m.seek(0)
            self.assertEqual(m.read_byte(), ord('a'))
            m.seek(0)
            self.assertEqual(m.readline(), b'a')
            m.seek(0)
            self.assertEqual(
