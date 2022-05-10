import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared')
import os
import sys
import time
import unittest
import warnings
from test import support
from test.support import TESTFN, run_unittest, import_module, \
    get_attribute, unlink, cpython_only
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support.os_helper import TESTFN_UNICODE, TESTFN_ENCODING

try:
    import _testcapi
except ImportError:
    _testcapi = None

# Skip tests if the _sqlite3 module wasn't built.
_sqlite3 = support.import_module('_sqlite3')

# Skip tests if the _sqlite module was built without the
# SQLITE_HAS_CODEC flag.
try:
    _sqlite3.sqlite_version_info
except AttributeError:
    raise unittest.SkipTest("_sqlite3 module was not built with the "
                            "SQLITE_HAS_CODEC flag")
