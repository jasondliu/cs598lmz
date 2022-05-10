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
from test.support import TESTFN, run_unittest, unlink, import_module

# Base class for testing a raw I/O implementation.
#
# The setUp() method creates a temporary file and sets data, the
# file's contents for testing.
#
# The tearDown() method closes the file if it is still open and
# deletes the temporary file.
#
# The test methods assume that the first 5 bytes of the file contain
# the ASCII characters "abcde".  If the file is not at least 5 bytes
# long, the test methods will fail.

class BaseRawIO(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for use by the tests.
        fd, self.fname = tempfile.mkstemp(".txt", "tmp")
        os.close(fd)
        with open(self.fname, "wb") as f:
            f.
