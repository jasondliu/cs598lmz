import mmap
# Test mmap.mmap.resize
import os
import unittest
from test import support

PAGESIZE = mmap.PAGESIZE

class MmapTests(unittest.TestCase):
    def _check_py_resize(self, map):
        size = map.size()
        map.resize(size + 1)
        self.assertEqual(map.size(), size + 1)
        map.resize(size + 2)
        self.assertEqual(map.size(), size + 2)
        map.resize(size + 3)
        self.assertEqual(map.size(), size + 3)
        map.resize(size + 1)
        self.assertEqual(map.size(), size + 1)
        map.resize(size)
        self.assertEqual(map.size(), size)
        map.resize(size - 1)
        self.assertEqual(map.size(), size - 1)
        map.resize(size - 2)
        self.assertEqual(map.size(), size - 2)
