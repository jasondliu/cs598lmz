import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import io
import os
import sys
import errno
import tempfile
import warnings
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Base class for testing io.RawIOBase
class RawIOTest:
    # Subclass must override
    def new_instance(self):
        raise NotImplementedError

    def test_read(self):
        rawio = self.new_instance()
        self.assertRaises(TypeError, rawio.read)
        self.assertRaises(TypeError, rawio.read, 'x')

    def test_readinto(self):
        rawio = self.new_instance()
        b = bytearray(10)
        self.assertRaises(TypeError, rawio.readinto)
        self.assertRaises(TypeError, rawio.readinto, 'x')
        self.assertRaises(TypeError, raw
