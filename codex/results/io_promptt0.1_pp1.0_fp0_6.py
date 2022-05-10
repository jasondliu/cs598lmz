import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_close(self):
        io.RawIOBase().close()

    def test_closed(self):
        raw = io.RawIOBase()
        self.assertFalse(raw.closed)
        raw.close()
        self.assertTrue(raw.closed)

    def test_detach(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.detach)
        raw.close()
        self
