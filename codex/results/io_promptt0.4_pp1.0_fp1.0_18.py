import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A complete implementation of RawIOBase is in io.BytesIO.

class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, _io.RawIOBase)
        self.assertRaises(TypeError, _io.RawIOBase, "not None or a buffer")

    def test_read(self):
        rawio = _io.BytesIO(b"abc")
        self.assertEqual(rawio.read(0), b"")
        self.assertEqual(rawio.read(1), b"a")
        self.assertEqual(rawio.read(2), b"bc")
        self.assertEqual(rawio.read(4), b"")
        self.assertEqual(rawio.read(), b"")
        self.assertEqual(rawio.read(1), b"")

    def test_readinto(self):
        rawio = _io.
