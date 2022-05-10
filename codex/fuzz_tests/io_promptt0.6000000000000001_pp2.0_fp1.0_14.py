import io
# Test io.RawIOBase.readinto

import io
import _pyio as pyio
import unittest
import test.support

class TestRawIOBase(unittest.TestCase):
    def test_readinto(self):
        buf = bytearray(b"abcdef")
        b = io.BytesIO(b"defghi")
        n = b.readinto(buf, 3)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"abcdefghi")
        self.assertEqual(b.tell(), 3)
        b = io.BytesIO(b"jkl")
        n = b.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"abcdefghijkl")
        self.assertEqual(b.tell(), 3)
        b = io.BytesIO(b"")
        n = b.readinto(buf)
        self.assertEqual(n, 0)
        self.assertEqual(buf, b"abcdefghij
