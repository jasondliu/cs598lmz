import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test RawIOBase implementation
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, rawio.readline)
        self.assertRaises(io.UnsupportedOperation, rawio.write, b'')
        self.assertRaises(io.UnsupportedOperation, rawio.seek, 0)
        self.assertRaises(io.UnsupportedOperation, rawio.tell)
        self.assertRaises(io.UnsupportedOperation, rawio.truncate)
        self.assertRaises(io.UnsupportedOperation, rawio.fileno)
        self.assertRaises(io.UnsupportedOperation, rawio.isatty)
        self.
