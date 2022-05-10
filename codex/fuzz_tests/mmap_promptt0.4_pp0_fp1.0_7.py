import mmap
# Test mmap.mmap(fileno, length, prot=PROT_READ, access=ACCESS_COPY)
#
# Create a file with some data in it, then mmap the file and verify
# that mmap'ed data matches the original data.

import os
import mmap
import unittest
import tempfile

from test import test_support

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.f = tempfile.TemporaryFile()
        self.f.write('\x00' * 10000)
        self.f.flush()
        self.f.seek(0)
        self.m = mmap.mmap(self.f.fileno(), 10000, access=mmap.ACCESS_WRITE)

    def tearDown(self):
        self.m.close()
        self.f.close()

    def test_find(self):
        self.m.seek(0)
        self.assertEqual(self.m.find('foo'), -1)
        self.assertEqual(self.m.
