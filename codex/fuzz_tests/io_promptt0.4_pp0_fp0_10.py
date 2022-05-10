import io
# Test io.RawIOBase

import io
import unittest
import weakref
from test import support

class RawIOBaseTest(unittest.TestCase):

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_abc_override(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b""
        self.assertRaises(io.UnsupportedOperation, MyRawIO().readinto)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().read1, 100)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().write, b"")
        self.assertRaises(io.UnsupportedOperation, MyRawIO().seek, 0)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().tell)
        self.assertRaises(io.UnsupportedOperation, MyRawIO().truncate)
        self.assertRaises(io.UnsupportedOperation, MyRawIO
