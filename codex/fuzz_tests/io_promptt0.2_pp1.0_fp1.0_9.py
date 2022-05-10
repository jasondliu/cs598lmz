import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation.
# Subclasses must override read, readinto, write and seek.
class BaseRawIOBaseTests(object):
    def setUp(self):
        self.f = self.IOCls(TESTFN, "wb+")

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def test_attributes(self):
        self.assertEqual(self.f.mode, "wb+")
        self.assertEqual(self.f.name, TESTFN)
        self.assertEqual(self.f.closed, False)

    def test_read(self):
        self.assertRaises(TypeError, self.f.read)
        self.assertRaises(TypeError, self.f.read, 10, 20)
        self.assertRaises(ValueError, self.
