import io
# Test io.RawIOBase

import os
import sys
import unittest
import warnings
from test import support
from test.support import TESTFN, run_unittest

# Skip test if io module is missing.
io = support.import_module('io')

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().write, b'')

    def test_constructor(self):
        self.assertRaises(TypeError, io.RawIOBase)

    def test_unsupported_operations(self):
        raw = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, raw.fileno)
        self.assertRaises(io
