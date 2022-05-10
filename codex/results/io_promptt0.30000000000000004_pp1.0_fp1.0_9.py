import io
# Test io.RawIOBase

import unittest
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok

import io
import os
import sys
import tempfile
import time
import warnings

# A mixin class for testing io.RawIOBase.
class RawIOMixin:

    # Subclasses must override.
    def raw_io_class(self):
        raise NotImplementedError

    def test_read(self):
        f = self.raw_io_class()
        self.assertRaises(io.UnsupportedOperation, f.read)

    def test_readinto(self):
        f = self.raw_io_class()
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())

    def test_write(self):
        f = self.raw_io_class()
        self.assertRaises(io.UnsupportedOperation, f.write, b'')

    def test_fileno(self):
        f = self.raw_io_class
