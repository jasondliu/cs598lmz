import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Base class for testing io.RawIOBase.
# The class should override read, readall and readinto.
class RawIOTest:
    # A concrete implementation of RawIOBase is needed to test readinto.
    # This is a no-op implementation.
    class RawIO(io.RawIOBase):
        def read(self, n=-1):
            return b""

        def readall(self):
            return b""

        def readinto(self, b):
            return 0

    def setUp(self):
        self.ioclass = self.RawIO
        self.io = self.ioclass()

    def test_read(self):
        self.assertRaises(TypeError, self.io.read)
        self.assertEqual(self.io.read(None), b"")
        self.assertEqual(self.io.read(0), b"")
        self.
