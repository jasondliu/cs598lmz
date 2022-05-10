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

# Base class for testing a RawIOBase implementation.
# Subclasses must override read(), readall() and write() as needed.
class BaseRawIOBaseTests(object):

    def test_constructor(self):
        # No default constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.io.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readinto, bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, self.io.readall)

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.io.write, b"")

    def test_fileno(self):
        self
