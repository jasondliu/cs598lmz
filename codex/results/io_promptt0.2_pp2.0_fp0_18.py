import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import import_module

# Skip test if _io module doesn't exist.
_io = import_module('_io')

class RawIOTest(unittest.TestCase):

    def test_read(self):
        # Test reading
        rawio = _io.RawIOBase()
        self.assertRaises(IOError, rawio.read)
        self.assertRaises(IOError, rawio.read, 10)
        self.assertRaises(IOError, rawio.read, 0)
        self.assertRaises(TypeError, rawio.read, 'foo')
        self.assertRaises(TypeError, rawio.read, None)

    def test_readinto(self):
        # Test reading into
        rawio = _io.RawIOBase()
        b = bytearray(10)
        self.assertRaises(IOError, rawio.readinto, b)
        self.assertRaises(TypeError, rawio.readinto, memoryview(b))

