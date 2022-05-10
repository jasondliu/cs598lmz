import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import errno
import _io

from test import support

# Base class for testing.  Doesn't define read() or readline() --
# derived classes must do that.
class BaseTestRawIO(object):

    def test_constructor(self):
        rawio = self.RawIOClass(self.initargs)
        self.assertEqual(rawio.mode, 'r')

    def test_read(self):
        rawio = self.RawIOClass(self.initargs)
        self.assertRaises(io.UnsupportedOperation, rawio.read)

    def test_readinto(self):
        rawio = self.RawIOClass(self.initargs)
        b = bytearray(self.size)
        n = rawio.readinto(b)
        self.assertEqual(n, self.size)
        self.assertEqual(b, self.get_sample_data())

    def test_readinto_array(self):
        import array

