import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref
import os
import sys
import tempfile
import errno
import warnings
from test import support
from test.support import TESTFN, run_unittest, unlink, import_module

# Base class for testing io.RawIOBase
class RawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = self.FileIO(TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertTrue(hasattr(self.f, 'name'))
        self.assertTrue(hasattr(self.f, 'mode'))
        self.assertTrue(hasattr(self.f, 'closed'))
        self.assertTrue(hasattr(self.f, 'close'))
        self.assertTrue(hasattr(self.f, 'fileno'))
        self.assertTrue(has
