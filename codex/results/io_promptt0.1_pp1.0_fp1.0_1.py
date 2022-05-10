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

# Base class for testing a RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseTestRawIO(object):
    def test_read(self):
        self.assertEqual(self.read(0), b'')
        self.assertEqual(self.read(1), b'x')
        self.assertEqual(self.read(2), b'xy')
        self.assertEqual(self.read(3), b'xyz')
        self.assertEqual(self.read(4), b'xyzw')
        self.assertEqual(self.read(5), b'xyzwx')
        self.assertEqual(self.read(6), b'xyzwxy')
        self.assertEqual(self.read(7), b'xyzwxyz')
        self.
