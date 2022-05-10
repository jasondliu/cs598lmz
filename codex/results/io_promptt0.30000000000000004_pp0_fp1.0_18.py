import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import tempfile
import shutil
import stat

from test import support
from test.support import TESTFN, unlink, run_unittest

# A mixin for testing RawIOBase
class BaseTestRawIO(object):
    # This is a mixin for testing RawIOBase.  It doesn't define setUp()
    # or tearDown(), nor does it define test_xxx() methods.

    def test_constructor(self):
        # No default constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_attributes(self):
        rawio = self.MockRawIO()
        self.assertIs(rawio.mode, None)
        self.assertIs(rawio.name, None)
        self.assertFalse(rawio.closed)

    def test_read(self):
        rawio = self.MockRawIO()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
