import io
# Test io.RawIOBase with a raw file descriptor

import os
import struct
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

import _io

# Test RawIOBase using a real file descriptor

try:
    os.urandom(1)
except NotImplementedError:
    raise unittest.SkipTest("os.urandom() is not implemented")

class TestRawIO(unittest.TestCase):
    def setUp(self):
        fd = os.open(TESTFN, os.O_RDWR | os.O_CREAT, 0o666)
        self.f = _io.FileIO(fd, closefd=True)
        buf = os.urandom(100000)
        self.f.write(buf)
        self.f.seek(0, 0)

    def tearDown(self):
        self.f.close()
        unlink(TESTFN)

    def test_read(self):
        buf = self.f.read(300)
        self.assertEqual(len(
