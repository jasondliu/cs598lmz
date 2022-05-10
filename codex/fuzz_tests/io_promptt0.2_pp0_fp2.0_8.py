import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        b = io.BytesIO(b"abc")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(1), b"a")
        self.assertEqual(b.read(2), b"bc")
        self.assertEqual(b.read(4), b"")
        self.assertEqual(b.read(0), b"")
        self.assertEqual(b.read(), b"")
        self.assertEqual(b.read(1), b"")

    def test_readall(self):
        b = io.BytesIO(b"abc")
        self.assertEqual(b.readall(), b"abc")
        self.assertEqual(b.readall(), b"")

    def test_readinto(self):
        b = io.BytesIO(b
