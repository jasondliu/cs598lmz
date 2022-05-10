import mmap
# Test mmap.mmap()
#
# This test is a bit different from the others.  It uses mmap to map a file
# into memory, and then uses the mmap object as a file object.  This is
# different from the other tests, which use file objects and then map them
# into memory.

import mmap
import os
import unittest
import tempfile

from test import test_support

# Create a file with some data to map.
data = 'abcdefghijklmnop' * 1024

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()
        f = open(self.filename, 'wb+')
        f.write(data)
        f.close()

    def tearDown(self):
        os.unlink(self.filename)

    def test_init(self):
        # mmap.mmap(fileno, length)
        f = open(self.filename, 'r+')
        m = mmap.mmap(f.fileno(), 16)
        self
