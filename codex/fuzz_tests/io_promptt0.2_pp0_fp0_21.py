import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Read at most 0 bytes.
        rawio = _io.RawIOBase()
        self.assertRaises(IOError, rawio.read, 0)

    def test_readinto(self):
        # Read at most 0 bytes.
        rawio = _io.RawIOBase()
        b = bytearray(1)
        self.assertRaises(IOError, rawio.readinto, b)

    def test_readall(self):
        rawio = _io.RawIOBase()
        self.assertRaises(IOError, rawio.readall)

    def test_read1(self):
        rawio = _io.RawIOBase()
        self.assertRaises(IOError, rawio.read1, 10)

    def test_readable(self):
        rawio = _io.RawIOBase()
        self.assertRaises(IOError
