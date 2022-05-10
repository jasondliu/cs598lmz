import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import weakref
import warnings

from test import support
from test.support import import_helper
from test.support.script_helper import assert_python_ok

# Skip tests if _testcapi is not available.
testcapi = import_helper.import_module('_testcapi')

# All tests are run twice: once for a text stream, and once for a
# binary stream.
TEST_TYPES = {io.TextIOWrapper: 't', io.BufferedReader: 'b'}

# A couple of callables useful for testing
def fake_fail():
    raise OSError

def fake_closed_file(*args, **kwargs):
    raise ValueError("I/O operation on closed file.")

class AutoFileTests(unittest.TestCase):
    # Tests for files that are automatically opened and closed
    # by the test harness.

    def setUp(self):
        self.f = io.BytesIO()

    def tearDown(self
