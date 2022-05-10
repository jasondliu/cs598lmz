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
# Subclasses must override read(), readinto() and seek() to
# run the full test suite.
class BaseRawIOBaseTests(object):

    def setUp(self):
        self.iobase = self.io.RawIOBase()
        self.iobase.__init__()
        self.iobase.close = lambda: 42
        self.iobase.fileno = lambda: 42
        self.iobase.isatty = lambda: False
        self.iobase.readable = lambda: True
        self.iobase.seekable = lambda: True
        self.iobase.writable = lambda: True
        self.iobase.read = self.read
        self.iobase.readinto = self.readinto
        self.iobase.seek =
