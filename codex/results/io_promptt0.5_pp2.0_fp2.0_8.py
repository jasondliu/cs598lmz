import io
# Test io.RawIOBase

import io
import sys
import unittest

from test.support import run_unittest, open_urlresource, check_warnings

class RawIOTest(unittest.TestCase):

    def test_read(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.read)
        self.assertRaises(io.UnsupportedOperation, r.read, 0)

    def test_readinto(self):
        r = io.RawIOBase()
        b = bytearray(10)
        self.assertRaises(io.UnsupportedOperation, r.readinto, b)
        self.assertRaises(TypeError, r.readinto, memoryview(b))

    def test_write(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.write, b'')

    def test_seek(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.seek
