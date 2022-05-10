import _struct
# Test _struct.Struct
from test.test_support import run_unittest, import_module, import_fresh_module
from test import test_support
from test.script_helper import assert_python_ok, assert_python_failure

import sys
import platform
import string
import unittest
import warnings

import doctest

test_support.requires("audio")

try:
    import _testcapi
except ImportError:
    _testcapi = None

if _testcapi is not None:
    from _testcapi import _get_error_mode, _set_error_mode

# Silence pyflakes
(assert_python_ok, assert_python_failure, test_support,
 unittest, doctest, _testcapi)

# Test _struct.Struct

class StructTest(unittest.TestCase):

    def test_unpack(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            st = _struct.Struct('bBhHiIlLqQfd')
        self
