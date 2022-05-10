import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys

from test import test_support
from test.test_support import TESTFN, run_unittest

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        try:
            os.remove(TESTFN)
        except OSError:
            pass

    def testWeakRefs(self):
        # verify weak references
        p = weakref.proxy(self.f)
        self.assertEqual(p.fileno(), self.f.fileno())
        self.assertEqual(p.closed, self.f.closed)
        f = self.f
        self.f = None
        self.assertRaises(ReferenceError, getattr, p, 'tell')
        self.f = f
        self.assertEqual(p.closed, self.f.
