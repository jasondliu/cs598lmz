import io
# Test io.RawIOBase and io.BufferedIOBase

import _io
import unittest
import weakref
import os
import sys
import pickle
import tempfile
import contextlib
import gc
import random
import io

from test import support
from test.support import import_module


# Base class for testing io objects.

class BaseTestIO(object):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.fname = os.path.join(self.tempdir, "test_io_base")
        self.f = open(self.fname, "w+b")
        self.f.write(b"abc")
        self.f.seek(0)

    def tearDown(self):
        self.f.close()
        support.rmtree(self.tempdir)

    def test_invalid_operations(self):
        self.assertRaises(TypeError, self.f.readinto, "")
        self.assertRaises(TypeError, self.f.readinto, memoryview(b""
