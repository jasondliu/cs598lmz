import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, _io.RawIOBase)

    def test_abc(self):
        # Test abstract methods
        rawio = _io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, rawio.readline)
        self.assertRaises(io.UnsupportedOperation, rawio.write, b"")
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate, 0)
        self.assertRaises(io.
