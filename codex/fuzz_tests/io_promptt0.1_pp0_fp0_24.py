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
# Subclasses must override read(), readinto() and seek().
class BaseRawIOBaseTests(object):

    def test_read(self):
        b = self.io.read(1)
        self.assertEqual(b, b"a")
        b = self.io.read(5)
        self.assertEqual(b, b"bcdef")
        b = self.io.read(1)
        self.assertEqual(b, b"g")
        b = self.io.read(1)
        self.assertEqual(b, b"")

    def test_readall(self):
        b = self.io.readall()
        self.assertEqual(b, b"abcdefg")
        b = self.io.readall()
        self.assert
