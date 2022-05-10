import mmap
# Test mmap.mmap
from mmap import *

from test import mapping_tests

from sys import getpagesize

class MmapTests(unittest.TestCase):

    def test_constructor(self):
        # The code below once caused a segfault.
        m = mmap.mmap(-1, 0)
        m.close()

    def test_find(self):
        m = mmap.mmap(-1, 0)
        self.assertRaises(ValueError, m.find, b'xyz')
        m.close()

    def test_move(self):
        m = mmap.mmap(-1, 0)
        self.assertRaises(ValueError, m.move, 0, 0, 0)
        m.close()

    def test_size(self):
        m = mmap.mmap(-1, 0)
        self.assertEqual(0, m.size())
        m.close()

    def test_resize(self):
        m = mmap.mmap(-1, 0)
        self.assertRaises(
