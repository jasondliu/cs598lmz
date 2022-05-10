import mmap
# Test mmap.mmap.resize

import mmap
import unittest
from test import support

try:
    mmap.mmap.resize
except AttributeError:
    raise unittest.SkipTest('mmap.mmap.resize not available')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.f = support.make_file(self.filename)
        self.f.write(b'\x00' * self.size)
        self.f.flush()
        self.m = mmap.mmap(self.f.fileno(), self.size)

    def tearDown(self):
        self.m.close()
        self.f.close()

    def test_resize(self):
        self.m.resize(self.size * 2)
        self.assertEqual(self.m.size(), self.size * 2)

    def test_resize_smaller(self):
        self.m.resize(self.size - 1)
