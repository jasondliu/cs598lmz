import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that read() returns an empty bytes object on EOF
        r = io.RawIOBase()
        self.assertEqual(r.read(1), b'')
        self.assertEqual(r.read(0), b'')
        self.assertEqual(r.read(-1), b'')
        self.assertEqual(r.read(), b'')

    def test_readinto(self):
        # Test that readinto() returns 0 on EOF
        r = io.RawIOBase()
        b = bytearray(10)
        self.assertEqual(r.readinto(b), 0)
        self.assertEqual(r.readinto(b), 0)
        self.assertEqual(r.readinto(b), 0)
        self.assertEqual(r.readinto(b), 0)

    def test_readinto_resize(self):
        # Test
