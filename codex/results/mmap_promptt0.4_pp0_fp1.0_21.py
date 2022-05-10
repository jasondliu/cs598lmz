import mmap
# Test mmap.mmap
import os
import sys
import time
import unittest
from test import support
from test.support import TESTFN, unlink
try:
    import threading
except ImportError:
    threading = None

try:
    import mmap
except ImportError:
    mmap = None


class MmapTests(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_badargs(self):
        self.assertRaises(TypeError, mmap.mmap, 1, 2)
        self.assertRaises(TypeError, mmap.mmap, 1, 2, 3, 4, 5, 6, 7)
        self.assertRaises(ValueError, mmap.mmap, -1, 1)
        self.assertRaises(ValueError, mmap.mmap, 1, -1)
        size = mmap.PA
