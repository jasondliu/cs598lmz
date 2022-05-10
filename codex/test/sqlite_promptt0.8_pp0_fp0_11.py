import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memorydb?mode=memory&cache=shared', uri=True)

try:
    import fcntl
except ImportError:
    print("No fcntl on this platform")

import unittest
import os
import os.path
import random
import string
import tempfile
import uuid
import sys

from test.test_support import (
    TESTFN, findfile, import_module, get_attribute, run_unittest, cpython_only,
    run_with_locale
)
lib = ctypes.CDLL(ctypes.util.find_library("sqlite3"))
ffi = ctypes.CDLL(None)._dl_get_ext_symbol("ffi")


threading.Thread(target=lambda: None).start()

# NOTE: if you get errors related to "out of memory" when running the tests
# under valgrind, use the following command line option for valgrind:
#
#   --suppressions=python.supp
#
# (see http://docs.python.org/dev/
