import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation.
# Subclasses must define a read() method.
class BaseRawIOTest(unittest.TestCase):
    def setUp(self):
        self.f = self.open()

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(TESTFN)

    def open(self):
        return self.io.open(TESTFN, "w+b", buffering=0)

    def test_read(self):
        self.assertEqual(self.f.read(0), b"")
        self.assertEqual(self.f.read(1), b"")
        self.assertEqual(self.f.read(10), b"")
        self.assertEqual(self.f.read(), b"")

    def test_readinto(self):
        b = bytearray(10
