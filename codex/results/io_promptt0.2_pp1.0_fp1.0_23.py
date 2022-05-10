import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import tempfile
import unittest
from test import support

# A mixin class to provide tests common to RawIOBase and BufferedIOBase
class BaseTestRawIO(object):
    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'foo')
        self.assertRaises(TypeError, self.io.read, b'foo', 'foo')
        self.assertRaises(TypeError, self.io.read, b'foo', 0, 'foo')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertRaises(ValueError, self.io.read, -1, 0)
        self.assertRaises(ValueError, self.io.read, -1, 0, 0)
        self.assertRaises(ValueError, self.io.read, 0, -1)
        self.assertRaises(ValueError, self.io
