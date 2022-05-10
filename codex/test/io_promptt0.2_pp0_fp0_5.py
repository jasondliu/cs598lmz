import io
# Test io.RawIOBase.readinto()

# Test basic functionality

import io
import _io
import unittest

class TestRawIO(unittest.TestCase):

    def test_readinto(self):
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")
        n = f.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b"abc")

    def test_readinto_resize(self):
        b = bytearray(b"abc")
        f = io.BytesIO(b)
        n = f.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b"abc")
        b.append(0)
        n = f.readinto(b)
        self.assertEqual(n, 0)
