import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)

    def test_readinto(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())

    def test_write(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.write, b'')

    def test_close(self):
        f = io.RawIOBase()
        f.close()
        self.assertRaises(ValueError, f.read)
        self.assertRaises(ValueError, f.readinto, bytearray())
        self.assertRaises(ValueError, f.write, b'')
        f.close()

    def test_fileno(self):
        f = io.RawIOBase()
        self
