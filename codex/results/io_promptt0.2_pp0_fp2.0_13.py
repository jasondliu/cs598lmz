import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings

from test import support

# Base class for testing a RawIOBase implementation.
# Subclasses must define a read() method.
class BaseRawIOTest(unittest.TestCase):

    def setUp(self):
        self.f = self.io.open(support.TESTFN, "w+b", buffering=0)

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(support.TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, "w+b")
        self.assertEqual(self.f.name, support.TESTFN)
        self.assertTrue(self.f.closed)

    def test_flush(self):
        self.assertRaises(io.UnsupportedOperation, self.f.flush)

    def test_fileno(self):
        self.assertRaises(io.Un
