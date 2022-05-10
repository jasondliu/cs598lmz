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
        self.assertEqual(len(b), 1)
        b = self.io.read(0)
        self.assertEqual(len(b), 0)
        b = self.io.read(-1)
        self.assertEqual(len(b), 0)
        b = self.io.read(10)
        self.assertEqual(len(b), 10)
        b = self.io.read(1000000)
        self.assertEqual(len(b), 0)

    def test_readinto(self):
        b = bytearray(10)
        n = self
