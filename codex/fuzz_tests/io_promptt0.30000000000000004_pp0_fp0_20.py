import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno

from test import support
from test.support import TESTFN, run_unittest

# A mixin for testing RawIOBase objects.
# Subclasses must define read(), readinto(), write(), seek(), and tell()
# methods.

class BaseTestRawIO(object):
    # The concrete class must define a writable and readable attribute.

    def test_read(self):
        b = self.readable.read(1)
        self.assertEqual(b, b'a')
        b = self.readable.read(0)
        self.assertEqual(b, b'')
        b = self.readable.read(2)
        self.assertEqual(b, b'bc')
        b = self.readable.read(4)
        self.assertEqual(b, b'defg')
        b = self.readable.read(1)
        self.assertEqual(b, b'')

    def test_readall(self):
        b =
