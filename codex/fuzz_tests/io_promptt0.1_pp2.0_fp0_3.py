import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class to provide tests common to RawIOBase and BufferedIOBase.
class BaseIOTest(object):

    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertRaises(TypeError, self.io.read, 'x')
        self.assertRaises(TypeError, self.io.read, None)
        self.assertRaises(TypeError, self.io.read, 1, 'x')
        self.assertRaises(TypeError, self.io.read, 1, None)
        self.assertRaises(TypeError, self.io.read, None, None)
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertRaises(ValueError, self.io.read, -1, -1)
        self.assertRaises(ValueError, self.io.read, -1, None)
