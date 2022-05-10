import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Base class for testing io.RawIOBase.
class RawIOTest:
    # Subclass must override.
    def new_io(self, *args):
        raise NotImplementedError

    def test_read(self):
        io = self.new_io()
        self.assertRaises(TypeError, io.read)
        self.assertRaises(TypeError, io.read, 'x')
        self.assertRaises(TypeError, io.read, None)
        self.assertRaises(TypeError, io.read, 10, None)
        self.assertRaises(ValueError, io.read, -1)
        self.assertRaises(ValueError, io.read, -10)
        self.assertRaises(ValueError, io.read, sys.maxsize + 1)
        self.assertRaises(ValueError, io.read, -sys.maxsize - 1)
