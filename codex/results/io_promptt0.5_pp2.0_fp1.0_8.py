import io
# Test io.RawIOBase

import unittest
import os
import sys
import io
import _pyio as pyio

from test import support
from test.support import import_helper, TESTFN, unlink, run_unittest

# Base for testing IO

class BaseTestIO(unittest.TestCase):

    def setUp(self):
        self.f = self.FileIO(TESTFN, 'w+')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertTrue(hasattr(self.f, 'mode'))
        self.assertTrue(hasattr(self.f, 'name'))

    def test_weakref(self):
        p = self.f
        f = self.f
        p = None
        f = None
        support.gc_collect()

    def test_flush_error_on_close(self):
        # Issue #16230
        f = self.f
        f.write(b
