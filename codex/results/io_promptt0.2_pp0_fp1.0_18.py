import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import import_module

# A mixin for RawIOBase tests that defines a simple read-write implementation
# using a bytearray.

class RawIOMixin:
    # A simple read-write implementation using a bytearray.

    def test_raw_read(self):
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(5), self.data[:5])
        self.assertEqual(self.io.read(5), self.data[5:10])
        self.assertEqual(self.io.read(5), self.data[10:15])
        self.assertEqual(self.io.read(5), self.data[15:20])
        self.assertEqual(self.io.read(1), b'')

    def test_raw_read1(self):
        self.assertEqual(self.io.read
