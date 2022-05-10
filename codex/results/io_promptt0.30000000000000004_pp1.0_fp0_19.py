import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# The tests in this file are intended to be run with the interpreter
# in isolated mode.

# Test RawIOBase

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # read([size])
        self.assertRaises(TypeError, io.RawIOBase().read)
        self.assertRaises(TypeError, io.RawIOBase().read, 'foo')
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read, 10)

    def test_readall(self):
        # readall()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readall)

    def test_readinto(self):
        # readinto(b)
        self.assertRaises(TypeError, io.RawIOBase().readinto)
        self.assertRaises(TypeError, io.RawIO
