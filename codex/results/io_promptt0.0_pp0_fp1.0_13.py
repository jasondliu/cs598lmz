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
    # the given mode.
    supports_read = True
    supports_readinto = True
    supports_seek = True

    def setUp(self):
        self.iobase = self.io.open(self.TESTFN, self.mode)

    def tearDown(self):
        if self.iobase is not None:
            self.iobase.close()
        support.unlink(self.TESTFN)

    def test_attributes(self):
        self.assertEqual(self.iobase.mode, self.mode)
        self.assertEqual(self.iobase.name, self.TESTFN)
        self.assertEqual(self
