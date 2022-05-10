import io
# Test io.RawIOBase

import _io
import unittest

class MyRawIOBase:
    def read(self, n=-1):
        return b"foo"

    def readall(self):
        return b"foo"

    def readinto(self, b):
        b[0:3] = b"foo"
        return 3

    def write(self, b):
        return len(b)

class RawIOBaseTest(unittest.TestCase):
    def test_constructor(self):
        b = io.RawIOBase()

    def test_abstract(self):
        b = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, b.read)
        self.assertRaises(io.UnsupportedOperation, b.readall)
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray(3))
        self.assertRaises(io.UnsupportedOperation, b.write, b"")

    def test_attributes(self):
        b = MyRawIOBase()
        _
