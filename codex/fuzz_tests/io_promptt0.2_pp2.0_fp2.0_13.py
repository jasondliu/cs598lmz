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
        self.assertRaises(TypeError, self.io.read, 0, 'x')
        self.assertRaises(ValueError, self.io.read, -1)
        self.assertRaises(ValueError, self.io.read, -1, 0)
        self.assertRaises(ValueError, self.io.read, 0, -1)
        self.assertEqual(self.io.read(0), b'')
        self.assertEqual(self.io.read(0, 0), b'')
        self.assertEqual(self.io.read(1), b'x')
       
