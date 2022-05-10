import io
# Test io.RawIOBase

from test import support
import unittest
from io import RawIOBase, SEEK_CUR, SEEK_SET

class RawIOTest(unittest.TestCase):
    def test_read(self):
        s = b"abcde"
        f = io.BytesIO(s)
        rawio = RawIOBase(f)
        self.assertEqual(rawio.read(0), b"")
        self.assertEqual(rawio.read(1), b"a")
        self.assertEqual(rawio.read(2), b"bc")
        self.assertEqual(rawio.read(3), b"de")
        self.assertEqual(rawio.read(4), b"")
        self.assertEqual(rawio.read(5), b"")

    def test_readinto(self):
        s = b"abcde"
        f = io.BytesIO(s)
        rawio = RawIOBase(f)
        b = bytearray(b"\0" * 100)
       
