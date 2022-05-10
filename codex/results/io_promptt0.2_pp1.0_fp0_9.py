import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import pickle

from test import support
from test.support import TESTFN, unlink

# A mixin for testing RawIOBase methods
class RawIOMixin:
    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertRaises(TypeError, self.io.read, 10, 'x')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(-1), b'')
        self.assertEqual(self.io.read(10), b'')

    def test_readinto(self):
        b = bytearray(10)
        self.assertRaises(TypeError, self.io.readinto)
        self.assertRaises
