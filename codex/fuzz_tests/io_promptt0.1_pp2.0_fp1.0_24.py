import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
import weakref

from test import support
from test.support import TESTFN, unlink

# A mixin for testing RawIOBase
class RawIOMixin:
    # The type to be tested
    rawio = None

    def setUp(self):
        self.f = self.rawio(TESTFN, "w+b")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_constructor(self):
        self.assertRaises(TypeError, self.rawio)
        self.assertRaises(TypeError, self.rawio, "foo", "r", 0, 0)
        self.assertRaises(TypeError, self.rawio, "foo", "r", buffering=0)
        self.assertRaises(TypeError, self.rawio, "foo", "r", encoding="ascii")
        self.assertRaises(TypeError, self.rawio
