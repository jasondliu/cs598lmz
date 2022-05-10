import io
# Test io.RawIOBase
#
# This test covers the RawIOBase interface, which deals with low-level
# unbuffered I/O.
#
# The tests are constructed so as to be able to run this test file directly,
# for debugging.

import io
import os
import sys
import unittest
from io import UnsupportedOperation
from test import support
from test.support import TESTFN, findfile, run_unittest

# A helper class to wrap file objects for the benefit of the tests
class FileWrapperIO(io.RawIOBase):
    def __init__(self, f):
        self.f = f
        self.mode = f.mode
        self.name = f.name
        self.closed = False

    def close(self):
        self.closed = True
        self.f.close()

    def fileno(self):
        return self.f.fileno()

    def isatty(self):
        return self.f.isatty()

    def readable(self):
        return 'r' in self.mode

    def writable(self):

