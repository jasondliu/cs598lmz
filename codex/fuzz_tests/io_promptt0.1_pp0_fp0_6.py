import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing io.RawIOBase.
# The class should override read(), readall() and readinto()
# (and optionally seek(), tell() and truncate()).
class RawIOTest:
    def setUp(self):
        self.f = self.io.open(TESTFN, "w+b", buffering=0)

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_read(self):
        self.f.write(b"abc")
        self.f.seek(0)
        self.assertEqual(self.read(self.f, 3), b"abc")
        self.assertEqual(self.read(self.f, 1), b"")

    def test_readall(self):
        self.f.write(b"abc")
        self.f.seek(0
