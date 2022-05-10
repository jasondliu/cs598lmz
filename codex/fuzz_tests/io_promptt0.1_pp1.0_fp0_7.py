import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import errno
import _io

from test import support
from test.support import TESTFN, run_unittest, import_module

# Base class for testing io.RawIOBase
class RawIOTest:
    # Subclass must override
    def new_io(self):
        raise NotImplementedError

    def test_read(self):
        io = self.new_io()
        self.assertRaises(TypeError, io.read)
        self.assertRaises(TypeError, io.read, 'x')
        self.assertRaises(TypeError, io.read, None)
        self.assertRaises(TypeError, io.read, 10, None)
        self.assertRaises(ValueError, io.read, -10)
        self.assertRaises(ValueError, io.read, -1)

    def test_readinto(self):
        io = self.new_io()
        b = bytearray(10)
        self.assertRa
