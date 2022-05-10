import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# A mixin class for testing RawIOBase
class RawIOMixin:
    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertRaises(TypeError, self.io.read, 10, 'x')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(-1), b'')
        self.assertEqual(self.io.read(10), b'')
        self.assertEqual(self.io.read(), b'')
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(-1), b'')

