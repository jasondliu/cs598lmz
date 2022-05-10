import mmap
# Test mmap.mmap(0, 1, access=mmap.ACCESS_WRITE)

from test import support
import unittest

class MmapTests(unittest.TestCase):
    def setUp(self):
        self.filename = support.TESTFN
        fp = open(self.filename, 'w+')
        fp.write('\0' * support.DATAFILESIZE)
        fp.close()
        self.fp = open(self.filename, 'r+')
        self.size = support.DATAFILESIZE

    def tearDown(self):
        if self.fp is not None:
            self.fp.close()
        if self.filename is not None:
            support.unlink(self.filename)

    def test_bad_args(self):
        self.assertRaises(TypeError, mmap.mmap, 1, 2, 3, 4, 5)
        self.assertRaises(ValueError, mmap.mmap, -1, 2)
