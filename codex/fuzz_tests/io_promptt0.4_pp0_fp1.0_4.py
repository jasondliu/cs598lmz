import io
# Test io.RawIOBase.readinto()

import _io
import unittest
import weakref
import os
import sys

from test import support

class TestRawIO(unittest.TestCase):
    def test_readinto(self):
        b = bytearray(b'abc')
        f = io.BytesIO(b)
        n = f.readinto(b)
        self.assertEqual(n, len(b))
        self.assertEqual(b, bytearray(b'abc'))
        self.assertRaises(TypeError, f.readinto, memoryview(b'xyz'))

    def test_readinto_array(self):
        import array
        b = bytearray(b'abc')
        f = io.BytesIO(b)
        a = array.array('b', b'x'*len(b))
        n = f.readinto(a)
        self.assertEqual(n, len(b))
        self.assertEqual(a.tobytes(), b)

    def test_readinto
