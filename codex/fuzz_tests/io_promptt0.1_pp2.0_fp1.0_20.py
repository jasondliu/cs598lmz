import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test that read() returns an empty bytes object at EOF
        r = io.RawIOBase()
        self.assertEqual(r.read(1), b'')
        self.assertEqual(r.read(0), b'')
        self.assertEqual(r.read(), b'')

    def test_readinto(self):
        # Test that readinto() returns 0 at EOF
        r = io.RawIOBase()
        b = bytearray(1)
        self.assertEqual(r.readinto(b), 0)
        self.assertEqual(r.readinto(b), 0)
        self.assertEqual(r.readinto(b), 0)

    def test_readall(self):
        # Test that readall() returns an empty bytes object at EOF
        r = io.RawIOBase()
        self.assertEqual(r.readall(), b''
