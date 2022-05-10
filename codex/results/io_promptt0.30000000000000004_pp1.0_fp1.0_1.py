import io
# Test io.RawIOBase

import unittest
from test import support
import os

class RawIOBaseTestCase(unittest.TestCase):

    def test_readinto(self):
        class MyRawIO(io.RawIOBase):
            def __init__(self, buf):
                self.buf = buf
            def readinto(self, b):
                n = len(self.buf)
                b[:n] = self.buf
                return n
        b = bytearray(5)
        r = MyRawIO(b'abc')
        n = r.readinto(b)
        self.assertEqual(n, 3)
        self.assertEqual(b, b'abc\x00\x00')
        n = r.readinto(b)
        self.assertEqual(n, 0)
        self.assertEqual(b, b'abc\x00\x00')
        r = MyRawIO(b'abcdef')
        n = r.readinto(b)
        self.assertEqual(n, 5)
        self.
