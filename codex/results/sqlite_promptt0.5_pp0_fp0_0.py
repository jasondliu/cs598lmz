import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect(None)
import unittest
import os
import time
import sys
import warnings
from test import support
from test.support import import_module
from test.support import captured_stdout
from test.support import run_with_locale
from test.support import run_with_tz
from test.support import TESTFN, unlink, unload, verbose, \
    get_attribute, check_warnings
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure
from test.support.script_helper import assert_python_warnings
from test.support.script_helper import make_script
from test import script_helper

try:
    import _testcapi
except ImportError:
    _testcapi = None

# Skip tests if the _sqlite module wasn't built.
_sqlite = import_module('_sqlite3')

SQLITE_VERSION = _sqlite.sqlite_version_info

# Skip
