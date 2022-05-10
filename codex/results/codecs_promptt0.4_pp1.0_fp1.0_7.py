import codecs
# Test codecs.register_error()
import binascii
import os
import tempfile
import unittest
import warnings
from test import support
from test.support import import_helper
from test.support.script_helper import assert_python_ok

# The tests here are run with the locale C, so that we know exactly
# which encoding is used.
# Also, use UTF-8 for file names, so that we can test file names with
# non-ASCII characters.

def check_warnings(*args, **kwargs):
    """Helper to silence warnings.warn() calls."""
    return support.check_warnings(*args, **kwargs)

class TestIncrementalDecoder(unittest.TestCase):

    # _tested_errors is a list of error handlers that are known to work.
    # This list is extended by test_register_error.
    _tested_errors = ['strict', 'ignore', 'replace']

    def setUp(self):
        self.errors = 'strict'
        self.decode = lambda b, e=self.errors: b.decode('as
