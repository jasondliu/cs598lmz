import mmap
# Test mmap.mmap(fileno, 0, access=mmap.ACCESS_WRITE)
# test that we can write to the mmap file
import os
import tempfile
import unittest

from test import test_support

def create_unnamed_mmap(size=0):
    mapping = mmap.mmap(-1, size, access=mmap.ACCESS_WRITE)
    return mapping

class UnnamedMmapTests(unittest.TestCase):

    def test_anonymous_mmap(self):
        mapping = create_unnamed_mmap(2**16)
        mapping.close()

class MmapTests(unittest.TestCase):

    def setUp(self):
        fd, self.filename = tempfile.mkstemp()
        os.close(fd)
        self.mapping = None

    def tearDown(self):
        if self.mapping is not None:
            self.mapping.close()
        os.unlink(self.filename)

