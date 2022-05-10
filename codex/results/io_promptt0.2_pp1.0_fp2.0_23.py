import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import _pyio as pyio

from test import support

# Base class for testing a RawIOBase implementation
class BaseRawTests:
    # Subclass must define a RawIOBase implementation.
    # The implementation should accept an optional string argument
    # to use as raw IO buffer.

    def test_read(self):
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(1), b'\x00')
        self.assertEqual(self.io.read(2), b'\x01\x02')
        self.assertEqual(self.io.read(3), b'\x03\x04\x05')
        self.assertEqual(self.io.read(4), b'\x06\x07\x08\t')
        self.assertEqual(self.io.read(5), b'\n\x0b\x0c
