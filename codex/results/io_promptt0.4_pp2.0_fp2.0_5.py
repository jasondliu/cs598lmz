import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref

from test import support

class RawIOTest(unittest.TestCase):

    def test_rawio(self):
        # Issue #11458: _io.RawIOBase is an internal ABC.
        self.assertRaises(TypeError, _io.RawIOBase)
        self.assertRaises(TypeError, _io.RawIOBase)
        self.assertRaises(TypeError, _io.RawIOBase, None)
        self.assertRaises(TypeError, _io.RawIOBase, None, None)

    def test_read_non_blocking(self):
        # Issue #11458: _io.RawIOBase.read() and .readall() must be non-blocking.
        class NonBlockingIO(_io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, buf):
                raise BlockingIOError(errno.EAGAIN, "read would block")
        f = NonBlockingIO()
        self.assert
