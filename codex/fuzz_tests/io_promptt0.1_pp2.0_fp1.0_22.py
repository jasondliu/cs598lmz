import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Issue #7995: if the io module is reloaded, RawIOBase is no longer
# a base class of IOBase.
import importlib
importlib.reload(io)

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w+')

    def tearDown(self):
        if not self.f.closed:
            self.f.close()
        support.unlink(TESTFN)

    def test_weakref(self):
        f = self.f
        p = proxy = _io.FileIO(f.fileno(), f.mode)
        self.assertIs(proxy.__finalize__(), f)
        del f, proxy
        support.gc_collect()
        self.assertTrue(p.closed)

    def test_del(self):
        f = self
