import io
# Test io.RawIOBase

import io
import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read_write(self):
        b = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, b.read)
        self.assertRaises(io.UnsupportedOperation, b.read, 0)
        self.assertRaises(io.UnsupportedOperation, b.read, 0)
        self.assertRaises(io.UnsupportedOperation, b.read, 0)
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray())
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray(1))
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray(1))
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray(1))
        self.assertRaises(io.UnsupportedOperation, b.readinto, bytearray(1
