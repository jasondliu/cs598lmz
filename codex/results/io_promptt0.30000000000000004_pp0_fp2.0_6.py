import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import import_helper
from test.support.script_helper import assert_python_ok

# A mixin for RawIOBase tests
class RawIOMixin:

    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertEqual(self.io.read(0), b'')

    def test_readinto(self):
        b = bytearray(self.size)
        self.assertRaises(TypeError, self.io.readinto)
        self.assertRaises(TypeError, self.io.readinto, 'x')
        self.assertEqual(self.io.readinto(b), self.size)
        self.assertEqual(b, self.get_sample_bytes())

    def test_readall(self):
        self.assertEqual(self.
