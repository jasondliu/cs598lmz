import io
# Test io.RawIOBase

import io
import _pyio as pyio
import _testcapi
import unittest
import os
import sys
import errno
import tempfile

from test import support
from test.support import TESTFN, run_with_locale, unlink, unlink
from test.support.script_helper import assert_python_ok

from io import UnsupportedOperation, BlockingIOError, DEFAULT_BUFFER_SIZE

# Filename used for testing
fname = TESTFN

# Disambiguate TESTFN for parallel testing, while letting it remain a valid
# module name.
fname = "{}_{}_tmp".format(fname, os.getpid())

# Base class for testing a RawIO implementation.

class BaseRawIOTest:

    # Subclasses must override
    thetype = None

    # Optional overrides
    def test_truncate(self):
        try:
            self.f.truncate()
        except UnsupportedOperation:
            pass
        else:
            self.fail("truncate() didn't raise UnsupportedOperation
