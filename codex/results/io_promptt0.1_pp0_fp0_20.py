import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Test the RawIOBase implementation
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, f.readline)
        self.assertRaises(io.UnsupportedOperation, f.write, b"")
        self.assertRaises(io.UnsupportedOperation, f.seek, 0)
        self.assertRaises(io.UnsupportedOperation, f.tell)
        self.assertRaises(io.UnsupportedOperation, f.truncate)
        self.assertRaises(io.UnsupportedOperation, f.fileno)
        self.assertRaises(io.UnsupportedOperation, f.isatty)
        self.assertRaises(io
