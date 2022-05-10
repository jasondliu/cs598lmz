import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import _io
import warnings
from test import support
from test.support import TESTFN, unlink, run_unittest, check_warnings

# Decorate all test cases to hide the tests if the _io module isn't
# available.
requires_io_module = unittest.skipUnless(hasattr(_io, 'open'),
                                        'requires _io.open')

class AutoFileTests(unittest.TestCase):
    # file tests for which a file is opened using the 'with' statement.

    def setUp(self):
        unlink(TESTFN)

    def tearDown(self):
        if os.path.exists(TESTFN):
            os.unlink(TESTFN)

    def test_enter_exit(self):
        with open(TESTFN, "wb") as f:
            self.assertTrue(f.closed == False)
        self.assertTrue(f.closed == True)

    def test_no_close
