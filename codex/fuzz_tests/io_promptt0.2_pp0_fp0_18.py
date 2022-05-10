import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import errno
import io
import pickle
import struct
import tempfile
import warnings

from test import support
from test.support import TESTFN, run_unittest, unlink, import_module

# Base class for testing io.RawIOBase
class BaseRawTests(object):
    # Subclass must define a type attribute.

    def setUp(self):
        self.f = self.type(TESTFN, "wb", 0)
        self.f.__init__(TESTFN, "wb", 0)
        self.f.close()

    def tearDown(self):
        unlink(TESTFN)

    def test_invalid_constructor(self):
        self.assertRaises(TypeError, self.type)
        self.assertRaises(TypeError, self.type, "foo")
        self.assertRaises(TypeError, self.type, "foo", "bar", "baz")
        self.assertRaises(TypeError, self.
