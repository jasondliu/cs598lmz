import io
# Test io.RawIOBase.readinto

import _io
import io
import sys
import unittest

class ReadintoTest(unittest.TestCase):

    def test_readinto_with_bytearray(self):
        f = io.BytesIO(b"abc")
        b = bytearray(4)
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc\x00")

    def test_readinto_with_memoryview(self):
        f = io.BytesIO(b"abc")
        b = memoryview(bytearray(4))
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b.tobytes(), b"abc\x00")

    def test_readinto_with_bytearray_and_offset(self):
        f = io.BytesIO(b"abc")
        b = bytearray(10)
