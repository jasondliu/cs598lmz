import io
# Test io.RawIOBase.readinto()
# Test io.RawIOBase.readinto1()

import os, sys
import unittest
from test import support

class TestReadInto(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(b'123')
        self.assertEqual(io.BytesIO(b'abc').readinto(b), 3)
        self.assertEqual(b, b'abc')
        self.assertEqual(io.BytesIO(b'xyz').readinto(b), 3)
        self.assertEqual(b, b'xyz')
        self.assertEqual(io.BytesIO(b'').readinto(b), 0)
        self.assertEqual(b, b'xyz')
        self.assertEqual(io.BytesIO(b'123').readinto(b), 3)
        self.assertEqual(b, b'123')
        self.assertEqual(io.BytesIO(b'12345').readinto(b), 3)
        self.assert
