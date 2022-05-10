import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import shutil
import weakref
import warnings
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseRawIOTest:
    # Subclasses can override.
    filename = TESTFN

    def setUp(self):
        self.f = self.open(self.filename, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(self.filename)

    def open(self, *args):
        return io.open(*args)

    def test_read(self):
        self.f.write(b"abc")
        self.f.seek(0)
        self.assertEqual(self.f.read(None), b"abc")
