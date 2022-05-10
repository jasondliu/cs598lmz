import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# A mixin for RawIOBase subclasses that don't have a working
# readable() or writable() method.
class NoReadWrite:
    def readable(self):
        return False

    def writable(self):
        return False

class TestRawIOBase(unittest.TestCase):

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, _io.RawIOBase)

    def test_attributes(self):
        # No public constructor
        self.assertRaises(TypeError, _io.RawIOBase)

    def test_read(self):
        # Should at least override read() to raise OSError
        rawio = _io.RawIOBase()
        self.assertRaises(OSError, rawio.read)

    def test_readinto(self):
        # Should at least override readinto() to raise OSError
        rawio = _io.RawIOBase()
        self.assert
