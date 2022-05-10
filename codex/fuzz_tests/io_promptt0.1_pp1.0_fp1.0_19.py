import io
# Test io.RawIOBase

import unittest
from test import support
from io import RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Read nothing
        self.assertEqual(RawIOBase().read(0), b'')
        self.assertEqual(RawIOBase().read(), b'')
        self.assertEqual(RawIOBase().read(None), b'')
        self.assertEqual(RawIOBase().read(-1), b'')

        # Read something
        self.assertRaises(NotImplementedError, RawIOBase().read, 1)

    def test_readinto(self):
        # Read nothing
        b = bytearray(b'x' * 100)
        self.assertEqual(RawIOBase().readinto(b), 0)
        self.assertEqual(b, b'x' * 100)
        self.assertEqual(RawIOBase().readinto(b, 10), 0)
        self.assertEqual(b, b'x' * 100)
       
