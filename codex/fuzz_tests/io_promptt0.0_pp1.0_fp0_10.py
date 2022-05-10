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
# Subclasses must override read(), readinto() and seek().
class BaseTestRawIO(object):
    # Subclass may override to indicate that the implementation supports
    # the given length argument to readinto().
    readinto_length_supported = False

    def setUp(self):
        self.iobase = self.io.RawIOBase()
        self.iobase.__init__(self.FileIO(self.TESTFN, "w+b"))
        self.iobase.write(b"abcde")
        self.iobase.seek(0, 0)

    def tearDown(self):
        self.iobase.close()
        support.unlink(self.TESTFN)

    def test_read(self):
        self.assertEqual(self.iobase.read(0), b"")
       
