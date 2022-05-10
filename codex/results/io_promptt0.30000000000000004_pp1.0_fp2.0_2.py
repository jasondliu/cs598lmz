import io
# Test io.RawIOBase

import _io
import io
import sys
import unittest
import weakref
import warnings

from test import support
from test.support import TESTFN, unlink

# Base class for testing io.RawIOBase.
# To test a concrete RawIO implementation, subclass this and override
# setUp(), tearDown(), and possibly RawIOClass.
class RawIOTest:

    # A RawIO class to test.  This must be set by the subclass.
    RawIOClass = None

    def setUp(self):
        self.f = self.RawIOClass(TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertTrue(self.f.mode == "w+b")
        self.assertTrue(self.f.name == TESTFN)

    def test_close(self):
        self.f.close()
        self.assertTrue(self.f.closed)
        self.assertRa
