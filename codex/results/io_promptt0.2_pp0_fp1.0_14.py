import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that read() returns empty bytes when passed a 0 byte count
        r = io.RawIOBase()
        self.assertEqual(r.read(0), b'')

    def test_readinto(self):
        # Test that readinto() returns 0 when passed a 0 byte count
        r = io.RawIOBase()
        b = bytearray(10)
        self.assertEqual(r.readinto(b, 0), 0)

    def test_readall(self):
        # Test that readall() returns empty bytes
        r = io.RawIOBase()
        self.assertEqual(r.readall(), b'')

    def test_readinto_resize(self):
        # Test that readinto() resizes the buffer
        r = io.RawIOBase()
        b = bytearray(10)
        self.assertRaises(TypeError, r.readinto, b)
