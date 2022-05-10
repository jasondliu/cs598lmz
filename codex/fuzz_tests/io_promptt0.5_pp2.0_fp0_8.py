import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        r = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, r.read)
        self.assertRaises(io.UnsupportedOperation,
                          r.read, b'x', 1)
        self.assertRaises(io.UnsupportedOperation, r.readall)
        self.assertRaises(io.UnsupportedOperation, r.readinto, b'x')
        self.assertRaises(io.UnsupportedOperation, r.readinto, bytearray(b'x'))
        self.assertRaises(io.UnsupportedOperation, r.read1, 1)
        self.assertRaises(io.UnsupportedOperation, r.readall)
        self.assertRaises(io.UnsupportedOperation, r.readline)
        self.assertRaises(io.UnsupportedOperation, r.readlines)
        self.assertRaises(io.UnsupportedOperation, r
