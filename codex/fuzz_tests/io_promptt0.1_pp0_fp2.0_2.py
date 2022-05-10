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
# Subclasses must override read(), readall() and write() as needed.
class BaseRawIOBaseTests(object):

    def test_rawiobase(self):
        # Read and write a short string
        self.assertEqual(self.read(7), b"testing")
        self.assertEqual(self.readall(), b"")
        self.write(b"more")
        self.assertEqual(self.read(3), b"mor")
        self.assertEqual(self.readall(), b"e")
        self.write(b"data")
        self.assertEqual(self.read(4), b"data")
        self.assertEqual(self.readall(), b"")
        self.write(b"1234567890")
        self.assertE
