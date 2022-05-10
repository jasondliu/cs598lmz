import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import pickle
import struct
import tempfile
import warnings
from test import support
from test.support import import_helper
from test.support.script_helper import assert_python_ok

# Base class for testing io.RawIOBase.
# The test_xxx() methods are expected to be overridden in subclasses.
class RawIOTest:

    def setUp(self):
        self.f = self.io.open(support.TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(support.TESTFN)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray())

    def test_write(self):
        self.assertRaises(
