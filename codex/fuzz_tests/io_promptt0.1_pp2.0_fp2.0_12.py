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
from test.support import import_module

# Base class for testing a RawIOBase implementation.
# Subclasses must override read(), readall() and write().
class BaseRawIOBaseTests(object):

    def test_rawiobase(self):
        # test RawIOBase implementation
        self.assertTrue(issubclass(self.io.RawIOBase, io.IOBase))
        self.assertTrue(issubclass(self.io.RawIOBase, io.RawIOBase))
        self.assertTrue(issubclass(self.io.RawIOBase, io.BufferedIOBase))
        self.assertTrue(issubclass(self.io.RawIOBase, io.TextIOBase))

    def test_read(self):
        # test read()
        b = self.read(0)
        self.assertEqual(b, self.bytes())
        b = self.read(1
