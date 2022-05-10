import io
# Test io.RawIOBase

import unittest
from test import support

class RawIOTest(unittest.TestCase):

    def test_args(self):
        # Test that RawIOBase.__init__() checks its arguments
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        # Test that RawIOBase.read() checks its arguments
        rawio = io.RawIOBase()
        self.assertRaises(TypeError, rawio.read)
        self.assertRaises(TypeError, rawio.read, 'foo')

    def test_readinto(self):
        # Test that RawIOBase.readinto() checks its arguments
        rawio = io.RawIOBase()
        self.assertRaises(TypeError, rawio.readinto)
        self.assertRaises(TypeError, rawio.readinto, bytearray())
        self.assertRaises(TypeError, rawio.readinto, bytearray(), 'foo')

    def test_write(self):
        # Test that RawIOBase.
