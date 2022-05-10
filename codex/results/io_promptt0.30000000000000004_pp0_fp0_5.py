import io
# Test io.RawIOBase

import io
import unittest
import weakref

from test import support

# Base class for testing io.RawIOBase.
# This is not meant to be complete, but rather to provide a set of
# useful tools for testing concrete implementations.

class BaseRawIOBaseTests(unittest.TestCase):

    def setUp(self):
        self.r = self.io.open(support.TESTFN, "w+b", buffering=0)

    def tearDown(self):
        if self.r:
            self.r.close()
        support.unlink(support.TESTFN)

    def test_attributes(self):
        self.assertEqual(self.r.mode, "w+b")
        self.assertEqual(self.r.name, support.TESTFN)
        self.assertEqual(self.r.closed, False)

    def test_weakref(self):
        p = weakref.proxy(self.r)
        self.assertEqual(p.mode, "w+b")
        self
