import mmap
# Test mmap.mmap.resize()

import mmap
import os
import stat
import tempfile
import unittest

from test import support

class MmapTests(unittest.TestCase):

    def setUp(self):
        self.path = tempfile.mktemp()
        f = open(self.path, 'w+')
        f.write('\x00' * 1024)
        f.close()

    def tearDown(self):
        os.unlink(self.path)

    def test_resize(self):
        m = mmap.mmap(os.open(self.path, os.O_RDWR), 1024)
        m.resize(2048)
        self.assertEqual(m.size(), 2048)
        m.close()

    def test_resize_negative(self):
        m = mmap.mmap(os.open(self.path, os.O_RDWR), 1024)
        self.assertRaises(ValueError, m.resize, -1)
        m.close()

