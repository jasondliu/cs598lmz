import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read)
        self.assertRaises(io.UnsupportedOperation, RawIOBase().read, 0)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, b'')
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, bytearray(b''))
        self.assertRaises(io.UnsupportedOperation, RawIOBase().readinto, memoryview(b''))

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().write, b'')

    def test_seek(self):
        self.assertRaises(io.UnsupportedOperation, RawIOBase().seek, 0)

    def test_tell(self):
        self.assertRaises(io
