import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class to provide tests common to RawIOBase and BufferedIOBase.
class BaseTestIOBase:

    def test_constructor(self):
        # No default constructor
        self.assertRaises(TypeError, self.io.IOBase)

    def test_detach(self):
        # Test detach()
        rawio = self.MockRawIO()
        bufio = self.io.BufferedReader(rawio)
        self.assertIs(bufio.detach(), rawio)
        self.assertRaises(ValueError, bufio.detach)
        self.assertRaises(ValueError, bufio.read)
        self.assertRaises(ValueError, bufio.read, 0)
        self.assertRaises(ValueError, bufio.readline)
        self.assertRaises(ValueError, bufio.readline, '')
        self.assertRaises(ValueError, bufio.read
