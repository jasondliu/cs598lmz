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
class BaseRawTests(object):
    # Subclass must define a RawIOBase implementation.
    io_class = None

    def setUp(self):
        self.f = self.io_class()

    def tearDown(self):
        if self.f:
            self.f.close()
        self.f = None

    def test_attributes(self):
        self.assertTrue(hasattr(self.f, 'mode'))
        self.assertTrue(hasattr(self.f, 'name'))

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        b = bytearray(10)
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, b)

    def test
