import mmap
# Test mmap.mmap() by doing a simple "find" operation using the 'find' method
# of the mmap object.

import mmap
import os
import unittest
import pickle
from test import support

support.requires("mmap")

data = b"Hello Python!\n"

class AutoFileTests(unittest.TestCase):
    def setUp(self):
        self.f = support.TESTFN
        f = open(self.f, 'wb')
        f.write(data)
        f.close()

    def tearDown(self):
        os.unlink(self.f)

    def test_find(self):
        f = open(self.f, 'r+b')
        m = mmap.mmap(f.fileno(), 0)
        m.find(b'Python')
        m.find(b'Hello')
        m.find(b'Python', 1)
        m.find(b'Python', 1, 25)
        m.find(b'Python', 1, 24)
