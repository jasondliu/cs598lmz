import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# A mixin class that provides a few utility methods for testing
# RawIOBase-based I/O objects.

class RawIOTest:

    def setUp(self):
        self.f = self.io.open(TESTFN, 'wb', buffering=0)

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(TESTFN)

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, self.f.read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, self.f.readinto, bytearray(1))

    def test_write(self):
        self.assertRaises(io.UnsupportedOperation, self.f.write, b'')

    def test_seek(self):
        self.assertRaises(io.Unsupported
