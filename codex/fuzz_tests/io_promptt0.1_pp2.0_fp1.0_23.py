import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import _io

from test import support
from test.support import import_helper

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseRawIO:
    def test_read(self):
        self.assertEqual(self.read(0), b'')
        self.assertEqual(self.read(1), b'\0')
        self.assertEqual(self.read(2), b'\0\0')
        self.assertEqual(self.read(3), b'\0\0\0')
        self.assertEqual(self.read(4), b'\0\0\0\0')
        self.assertEqual(self.read(5), b'\0\0\0\0\0')
        self.assertEqual(self.read(6), b'\0\0\0\0\0\0')
        self.assertEqual
