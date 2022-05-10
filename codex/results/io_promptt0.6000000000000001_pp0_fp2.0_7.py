import io
# Test io.RawIOBase
#
# io.RawIOBase is an abstract class whose methods raise io.UnsupportedOperation.
# We test that these methods raise this exception.
#
# io.RawIOBase is the base class of io.BufferedIOBase, which is in turn the
# base class of io.FileIO and io.BytesIO.  io.BufferedIOBase overrides some
# of the abstract methods of io.RawIOBase, but not all; the ones it does not
# override should still raise io.UnsupportedOperation.
#
# Tested methods:
#   read, readinto, write, seek, tell, truncate, close
# Untested methods:
#   fileno -- this is not implemented in Python/pypy

import io
import sys
import unittest
import weakref

from . import test_support


class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        f = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, f.read)
        self.assertRaises(io.UnsupportedOperation
