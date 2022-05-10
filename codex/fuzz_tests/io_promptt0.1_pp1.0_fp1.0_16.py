import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
import errno

from test import support
from test.support import TESTFN, unlink

# Base class for testing a RawIOBase implementation.
# Subclasses must override read(), readall() and write() as needed.
class BaseRawIOBaseTests(object):

    def setUp(self):
        # Subclasses may override
        self.thetype = self.io.RawIOBase

    def tearDown(self):
        support.unlink(TESTFN)

    def test_attributes(self):
        f = self.thetype()
        self.assertEqual(f.mode, "")
        self.assertEqual(f.name, None)
        f.close()

    def test_bad_args(self):
        self.assertRaises(TypeError, self.thetype, "foo", 0, 0)
        self.assertRaises(TypeError, self.thetype, "foo", "bar")
        self.assertRaises(TypeError
