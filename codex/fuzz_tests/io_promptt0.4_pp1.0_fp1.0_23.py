import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read, 0)
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read, 0)
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read, 0)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, b'')
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, bytearray(b''))
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, memoryview(b''))
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, memoryview(bytearray(b'')))

    def test_
