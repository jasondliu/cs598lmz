import io
# Test io.RawIOBase

import _io
import sys
import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_args(self):
        # Should accept only string or None.
        self.assertRaises(TypeError, _io.RawIOBase)
        self.assertRaises(TypeError, _io.RawIOBase, 0)
        _io.RawIOBase('')
        _io.RawIOBase(None)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation,
                          _io.RawIOBase().readinto, bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, _io.RawIOBase().write, b'')
