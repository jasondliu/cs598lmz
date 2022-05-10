import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io

from test import test_support

# A mixin for testing raw I/O.
class RawIOMixin:

    def test_read(self):
        b = self.io.read(1)
        self.assertEqual(b, b"1")
        pos = self.io.tell()
        b = self.io.read(1)
        self.assertEqual(b, b"2")
        self.assertEqual(self.io.tell(), pos + 1)
        self.assertRaises(TypeError, self.io.read, "")
        self.assertRaises(TypeError, self.io.read, None)
        self.assertRaises(TypeError, self.io.read, 1, 2)
        self.assertRaises(TypeError, self.io.read, buffer=b"")
        self.assertRaises(TypeError, self.io.read, size="")
        self.assertRaises(Value
