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
from test.support import import_helper

# Base class for testing a RawIOBase implementation.
# The class to test is given as the 'io' class attribute.
#
# Subclasses must override readall() to exercise non-blocking
# behaviour.
class BaseRawTests(object):
    io = None

    def setUp(self):
        self.f = self.io(b"\0" * 100)

    def tearDown(self):
        self.f.close()

    def test_invalid_operations(self):
        # readinto() and read() must not be allowed on a write-only object
        self.assertRaises(io.UnsupportedOperation,
                          self.f.readinto, bytearray(b"x"))
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_write(self):
        self.assert
