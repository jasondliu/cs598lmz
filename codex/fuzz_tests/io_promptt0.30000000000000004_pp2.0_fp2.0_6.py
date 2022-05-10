import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_attributes(self):
        self.assertTrue(hasattr(io.RawIOBase, 'mode'),
                        "io.RawIOBase instance has no attribute 'mode'")
        self.assertTrue(hasattr(io.RawIOBase, 'name'),
                        "io.RawIOBase instance has no attribute 'name'")

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_close(self):
        raw = io.RawIOBase()
        self.assertFalse(raw.closed)
        raw.close
