import io
# Test io.RawIOBase

import sys
import os
import unittest
from test import support
from io import BytesIO, BufferedIOBase, UnsupportedOperation

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        b = BytesIO(b"abc")
        self.assertEqual(b.read(), b"abc")
        self.assertEqual(b.read(), b"")

    def test_readinto(self):
        b = BytesIO(b"abc")
        buf = bytearray(2)
        n = b.readinto(buf)
        self.assertEqual(n, 2)
        self.assertEqual(buf, b"ab")
        self.assertEqual(b.readinto(buf), 0)
        self.assertEqual(buf, b"ab")
        self.assertEqual(b.readinto(bytearray()), 0)

    def test_readinto_resize(self):
        b = BytesIO(b"abc")
        buf = bytearray
