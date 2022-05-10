import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Issue #7995: if the io module is imported before the _io module,
# the io.IOBase class won't be properly initialized.
import_io_before_test = 'io' in sys.modules

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w+')

    def tearDown(self):
        if not self.f.closed:
            self.f.close()
        support.unlink(TESTFN)

    def test_weakref(self):
        p = proxy = _io.FileIO(self.f.fileno(), self.f.mode)
        self.assertIs(proxy.__finalize__(), self.f)
        self.assertIs(proxy._finalizing, self.f)
        self.assertIs(proxy._finalized, self.f)
        self
