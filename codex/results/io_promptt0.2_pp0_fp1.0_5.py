import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys

from test import support
from test.support import import_helper

# Base for testing the RawIOBase ABC.
# To test a concrete RawIOBase implementation create a subclass and
# override read, readall and seek.
class BaseTestRawIO(object):
    # Constructor.  Can raise an exception or return a unusable stream.
    def setUp(self):
        self.r = self.io.open(support.TESTFN, 'w+b')

    def tearDown(self):
        if self.r:
            self.r.close()
        support.unlink(support.TESTFN)

    def test_attributes(self):
        self.assertTrue(hasattr(self.r, 'mode'))
        self.assertTrue(hasattr(self.r, 'name'))
        self.assertTrue(hasattr(self.r, 'close'))
        self.assertTrue(hasattr(self.r, 'closed'))
        self.assertTrue(
