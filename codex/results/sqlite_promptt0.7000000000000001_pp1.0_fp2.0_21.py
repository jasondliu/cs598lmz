import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("file::memory:?cache=shared", uri=True)
from sqlite3 import dbapi2 as sqlite
from sqlite3 import Error

from . import _sqlite3
import random
import time
from collections import defaultdict
from .test_threading_namespace import get_ident
import unittest
from test import support
from test.support import bigaddrspacetest, bigmemtest
from test.support import reraise_threading_exceptions
from test.support.script_helper import assert_python_ok
from test.support.threading_helper import wait_for_threads


# Filename used for testing
db_filename = support.TESTFN

# Disable the test if the pysqlite library is built without shared cache
# support.
test_shared_cache = support.detect_api_mismatch('sqlite3', 'sqlite_enable_shared_cache')

# Assert that the sqlite3 module is sane
support.import_module('sqlite3')

# Assert that the sqlite3 module is using the ctypes interface
