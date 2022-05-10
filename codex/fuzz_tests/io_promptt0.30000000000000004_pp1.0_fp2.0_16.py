import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import weakref
import warnings
import errno
import _testcapi

from test import test_support

# A mixin for testing RawIOBase.

class BaseRawTests(object):

    # Subclass is expected to define a suitable read() method.

    def test_read(self):
        self.assertEqual(self.read(0), "")
        self.assertEqual(self.read(5), self.sample[:5])
        self.assertEqual(self.read(len(self.sample)), self.sample)
        self.assertEqual(self.read(len(self.sample)+10), self.sample)
        self.assertEqual(self.read(0), "")

    def test_readinto(self):
        b = bytearray(self.sample)
        self.assertEqual(self.readinto(b), len(self.sample))
        self.assertEqual(b, self.sample)
        self.assertEqual(self.readinto
