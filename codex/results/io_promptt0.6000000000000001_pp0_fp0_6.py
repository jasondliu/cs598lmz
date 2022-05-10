import io
# Test io.RawIOBase.readinto()

import io, mmap
import os, os.path
import sys
import unittest

from test import support

class TestMmap(unittest.TestCase):

    def setUp(self):
        self.file = support.TESTFN
        f = open(self.file, 'wb')
        try:
            f.write(b'\0' * mmap.ALLOCATIONGRANULARITY)
        finally:
            f.close()

    def tearDown(self):
        support.unlink(self.file)

    def test_wrong_prot(self):
        f = open(self.file, 'r+b')
        self.assertRaises(ValueError, mmap.mmap, f.fileno(), 0,
                          access=mmap.ACCESS_READ)
        f.close()

    def test_resize(self):
        f = open(self.file, 'r+b')
        m = mmap.mmap(f.fileno(), 0)
        m.resize(1)

