import mmap
# Test mmap.mmap()
#
# This test is derived from the test case for mmap.mmap() in the
# Python 2.5.2 test suite.

import os
import unittest
import mmap
import tempfile
import struct

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = tempfile.mktemp()
        f = open(self.filename, 'wb+')
        try:
            f.write('\0' * mmap.PAGESIZE)
            f.flush()
            self.f = f
        except:
            f.close()
            os.unlink(self.filename)
            raise

    def tearDown(self):
        if self.f:
            self.f.close()
        if self.filename:
            os.unlink(self.filename)

    def test_basic(self):
        m = mmap.mmap(self.f.fileno(), mmap.PAGESIZE)
        m.write('hello world')
        m.seek(0)
