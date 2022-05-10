import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
import warnings
from test import support
from test.support import TESTFN, unlink

# Issue #11459: if the implementation supports the seek/tell methods,
# test them.
SEEK_TELL_SUPPORTED = hasattr(io.RawIOBase, 'seek') and hasattr(io.RawIOBase, 'tell')

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Reads up to size bytes from the object and returns them.
        # If the argument is omitted, None, or negative, reads and
        # returns all data until EOF.
        #
        # Returns an empty bytes object on EOF.
        #
        # Subclasses should override this method.
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.read)
        self.assertRaises(io.UnsupportedOperation, rawio.read, 10)

    def test_readinto(self):
        # Reads up to
