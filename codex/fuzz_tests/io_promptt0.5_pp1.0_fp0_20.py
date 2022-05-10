import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile

from test.test_support import TESTFN, run_unittest, findfile, import_module

# Base class for testing a raw I/O implementation.  This sets up the
# stream and provides a standard interface for the derived class to
# test.
class RawIOTest:
    # Subclasses can override.
    filename = TESTFN

    def setUp(self):
        # Create a test file.
        fp = open(self.filename, "wb")
        try:
            fp.write("abc\n")
            fp.write("abc\n")
        finally:
            fp.close()

    def tearDown(self):
        os.unlink(self.filename)

    def open(self, **kwargs):
        return io.open(self.filename, "r", **kwargs)

    def readall(self, stream):
        return stream.read()

    def readline(self, stream):
        return stream.readline()

    def readlines
