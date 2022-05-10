import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)

    def test_readinto(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())

    def test_write(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.write, b'')

    def test_close(self):
        f = io.RawIOBase()
        f.close()
        f.close()

    def test_closed(self):
        f = io.RawIOBase()
        self.assertFalse(f.closed)
        f.close()
        self.assertTrue(f.closed)

    def test_fileno(self):
        f = io.RawIO
