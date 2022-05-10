import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, _io.RawIOBase)
        self.assertRaises(TypeError, _io.RawIOBase, "foo")

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().write,
                          b"foo")

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(io.UnsupportedOperation, _
