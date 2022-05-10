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
# The class to be tested is given as the 'io' class attribute.
#
# Subclasses must override readall() to exercise non-blocking reads.
class RawIOTest(unittest.TestCase):
    io = None

    def setUp(self):
        self.f = self.io(b"1234567890")

    def tearDown(self):
        self.f.close()

    def test_attributes(self):
        self.assertEqual(self.f.mode, "rb")
        self.assertEqual(self.f.name, None)
        self.assertEqual(self.f.closed, False)

    def test_read(self):
        self.assertEqual(self.f.read(0), b"")
        self.assertEqual(self
