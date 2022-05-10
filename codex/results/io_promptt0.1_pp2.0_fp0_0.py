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
from test.support import TESTFN, unlink, run_unittest

# A mixin for testing RawIOBase
class BaseTestRawIO(object):
    # Subclasses must define a read() method.
    # They may also define setUp(), tearDown(), and __init__() as needed.

    def test_constructor(self):
        # No args
        self.assertRaises(TypeError, self.io.RawIOBase)

        # Too many args
        self.assertRaises(TypeError, self.io.RawIOBase, None, None)

    def test_read(self):
        # read() should return None at EOF
        self.assertEqual(self.read(0), b'')
        self.assertEqual(self.read(1), b'')
        self.assertEqual(self.read(100), b'')

        # readinto() should return 0 at EOF
        b
