import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation.
# Subclasses must override read, readinto and seek.
class BaseRawIOBaseTests(unittest.TestCase):
    def setUp(self):
        self.f = self.io.open(TESTFN, "w+b", buffering=0)

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, "w+b")
        self.assertEqual(self.f.name, TESTFN)
        self.assertEqual(self.f.buffer, None)
        self.assertEqual(self.f.raw.mode, "w+b")
        self.assertEqual(self.f.raw.name, TESTFN)
        self.assertEqual(self.f.raw.
