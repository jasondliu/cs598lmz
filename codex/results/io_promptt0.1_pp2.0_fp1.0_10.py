import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin for RawIOBase tests that need to create a file-like object.
class RawIOMixin:
    def setUp(self):
        self.f = self.IOCls(TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_constructor(self):
        self.assertRaises(TypeError, self.IOCls)
        self.assertRaises(TypeError, self.IOCls, "foo", 0, 0)
        self.assertRaises(ValueError, self.IOCls, "foo", "w", "foo")
        self.assertRaises(ValueError, self.IOCls, "foo", "w", -1)
        self.assertRaises(ValueError, self.IOCls, "foo", "w", 0, -1
