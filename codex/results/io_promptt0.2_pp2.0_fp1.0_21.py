import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class to provide tests common to RawIOBase and BufferedIOBase.
class BaseTestIOBase:

    def test_constructor(self):
        # No public constructor
        self.assertRaises(TypeError, self.io.IOBase)

    def test_detach(self):
        # No public constructor
        self.assertRaises(TypeError, self.io.IOBase)

    def test_readable(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.readable)

    def test_writable(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.writable)

    def test_seekable(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.seekable)

    def test_fileno(self):
        self.assertRaises(io.UnsupportedOperation, self.iobase.fil
