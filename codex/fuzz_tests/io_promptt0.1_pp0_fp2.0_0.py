import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class for RawIOBase tests.
class RawIOMixin:
    # Subclasses must define self.type2test

    def test_constructor(self):
        # No default constructor
        self.assertRaises(TypeError, self.type2test)

    def test_abstract(self):
        # Can't instantiate an abstract class
        self.assertRaises(TypeError, self.type2test, "foo")

    def test_read(self):
        # read()
        f = self.type2test(TESTFN)
        self.assertRaises(io.UnsupportedOperation, f.read)
        f.close()

    def test_readinto(self):
        # readinto()
        f = self.type2test(TESTFN)
        self.assertRaises(io.UnsupportedOperation, f.readinto, bytearray())
        f.close()

    def test_write
