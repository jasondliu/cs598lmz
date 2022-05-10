import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# A mixin class for RawIOBase tests.
class RawIOMixin:
    # Subclasses must define a RawIOBase class attribute.

    def test_constructor(self):
        # No default constructor
        self.assertRaises(TypeError, self.RawIOBase)

    def test_attributes(self):
        # Subclasses must define a readable and writable attribute.
        rawio = self.MockRawIO()
        self.assertIs(rawio.readable(), rawio.readable)
        self.assertIs(rawio.writable(), rawio.writable)
        self.assertIs(rawio.seekable(), rawio.seekable)

    def test_read(self):
        rawio = self.MockRawIO()
        self.assertRaises(io.UnsupportedOperation, rawio.read)

    def test_readinto(self):
        rawio = self.M
