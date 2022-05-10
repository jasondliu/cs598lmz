import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        b = io.BytesIO(b"ABCDE")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"A")
        self.assertEqual(b.read(2), b"BC")
        self.assertEqual(b.read(3), b"DE")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(1), b"")

    def test_readinto(self):
        b = io.BytesIO(b"ABCDE")
        buf = bytearray(b"\0"*10)
        self.assertEqual(b.readinto(buf), 5)
        self.assertEqual(buf, b"ABCDE\0\0\0\0\0")
        self.assertE
