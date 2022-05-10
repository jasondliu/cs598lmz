import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import contextlib
import errno

from test import support
from test.support import TESTFN, unlink, run_unittest

# Base test class for RawIOBase
class BaseTestRawIO(object):
    # The concrete class to test.
    io_class = None

    # If the concrete class is a subclass of BufferedIOBase, the buffer size
    # to use.
    buffer_size = None

    def test_read(self):
        b = self.io_class()
        self.assertRaises(io.UnsupportedOperation, b.read)
        self.assertRaises(io.UnsupportedOperation, b.read, 0)
        self.assertRaises(io.UnsupportedOperation, b.read, 0)
        self.assertRaises(io.UnsupportedOperation, b.read, 0)

    def test_readinto(self):
        b = self.io_class()
        self.assertRaises(io.UnsupportedOperation, b.readinto, byt
