import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(:memory:)
import sys
import pytest

# faulthandler module
try:
    from faulthandler import enable, dump_traceback_later
except ImportError:
    pytestmark = pytest.mark.skip("faulthandler module not available")

from StringIO import StringIO
from sqlite3 import OperationalError

import _sqlite3

lib = ctypes.util.find_library("sqlite3")
lib = ctypes.CDLL(lib)

dbname = os.path.join(os.path.dirname(__file__), "test.db")
