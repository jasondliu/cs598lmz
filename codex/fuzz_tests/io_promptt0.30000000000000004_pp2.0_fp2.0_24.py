import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest, unlink

# A mixin class for testing io.RawIOBase
class RawIOMixin:
    # Subclasses must define self.filename, self.mode, and self.bmode
    def setUp(self):
        self.f = io.open(self.filename, self.mode)
        self.f2 = io.open(self.filename, self.bmode)

    def tearDown(self):
        self.f.close()
        self.f2.close()
        unlink(self.filename)

    def test_read(self):
        self.assertEqual(self.f.read(1), b'a')
        self.assertEqual(self.f.read(1), b'b')
        self.assertEqual(self.f.read(1), b'c')
        self.assertEqual(self.f.read(1), b'd')
        self.assertEqual(
