import io
# Test io.RawIOBase readinto() method.
import sys
import unittest

class BytesIOTest(unittest.TestCase):

    def test_readinto(self):
        # test readinto()
        b = io.BytesIO(b"abc")
        buf = bytearray(2)
        n = b.readinto(buf)
        self.assertEqual(n, 2)
        self.assertEqual(buf, b"ab")
        n = b.readinto(buf)
        self.assertEqual(n, 1)
        self.assertEqual(buf, b"c\x00")
        n = b.readinto(buf)
        self.assertEqual(n, 0)
        self.assertEqual(buf, b"c\x00")

        # test readinto() with offset
        b = io.BytesIO(b"abc")
        buf = bytearray(4)
        n = b.readinto(buf, 1)
        self.assertEqual(n, 3)
        self.assertEqual(buf,
