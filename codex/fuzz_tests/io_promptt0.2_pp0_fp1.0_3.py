import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_unsupported(self):
        class MyRawIO(_io.RawIOBase):
            def readable(self):
                return True
            def writable(self):
                return True
            def seekable(self):
                return True
        self.assertRaises(io.UnsupportedOperation, MyRawIO().read)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, MyRawIO().write, b"")
        self.assertRaises(io.UnsupportedOperation, MyRawIO().seek, 0)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().tell)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().truncate
