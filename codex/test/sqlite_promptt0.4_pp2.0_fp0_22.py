import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import os
import sys
import time
import shutil
import tempfile
import subprocess
import unittest
import weakref
import logging

# Test the C extension module
if sys.platform == 'win32':
    from _sqlite3 import *
else:
    from sqlite3 import *

# Skip tests if _sqlite3 module wasn't built
try:
    from sqlite3 import _sqlite3
except ImportError:
    raise unittest.SkipTest("_sqlite3 module not available")

# Skip tests if the _sqlite3 module was not compiled with the
# SQLITE_ENABLE_COLUMN_METADATA option.
try:
    from sqlite3 import PARSE_COLNAMES
except ImportError:
    raise unittest.SkipTest("_sqlite3 module not compiled "
                            "with SQLITE_ENABLE_COLUMN_METADATA")

# Skip tests if the _sqlite3 module was not compiled with the
