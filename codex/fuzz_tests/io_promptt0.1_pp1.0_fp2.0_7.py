import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class for RawIOBase tests
class RawIOMixin:

    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertRaises(TypeError, self.io.read, 10, 'x')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(-1), b'')
        self.assertEqual(self.io.read(10), b'')
        self.assertEqual(self.io.read(-1), b'')
        self.assertEqual(self.io.read(sys.maxsize), b'')
        self.assertEqual(self.io.read(-1), b''
