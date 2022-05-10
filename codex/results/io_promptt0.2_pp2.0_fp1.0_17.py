import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# A mixin class to provide a default implementation of write()
# based on the read() method.
class Readable(object):
    def write(self, b):
        n = len(b)
        while n > 0:
            v = self.read(n)
            if not v:
                raise RuntimeError("write() on read-only stream")
            n -= len(v)

class RawIOTest(unittest.TestCase):

    def test_args(self):
        # Test RawIOBase constructor
        self.assertRaises(TypeError, io.RawIOBase)

    def test_read(self):
        # Test RawIOBase.read()
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        # Test RawIOBase.readinto()
        self.assertRaises(io.UnsupportedOperation, io.
