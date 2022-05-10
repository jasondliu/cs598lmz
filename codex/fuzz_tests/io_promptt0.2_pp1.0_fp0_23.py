import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import bigmemtest, bigaddrspacetest, TESTFN, unlink

# A mixin class for RawIOBase tests
class RawIOMixin:

    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertRaises(TypeError, self.io.read, 0, 'x')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertRaises(ValueError, self.io.read, -1, 0)
        self.assertRaises(ValueError, self.io.read, 0, -1)
        self.assertRaises(ValueError, self.io.read, -1, -1)
        self.assertRaises(ValueError, self.io.read, sys.maxsize+1)
        self.assertRaises(ValueError,
