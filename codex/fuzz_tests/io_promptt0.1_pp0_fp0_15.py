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
class BaseRawIOBaseTests(object):

    def test_read(self):
        b = self.io.read(1)
        self.assertEqual(len(b), 1)
        self.assertEqual(b, self.data[0:1])
        b = self.io.read(0)
        self.assertEqual(len(b), 0)
        self.assertEqual(b, self.data[0:0])
        b = self.io.read(-1)
        self.assertEqual(len(b), len(self.data))
        self.assertEqual(b, self.data)
        b = self.io.read()
        self.assertEqual(len(b), 0)
        self.assertEqual(b, self
