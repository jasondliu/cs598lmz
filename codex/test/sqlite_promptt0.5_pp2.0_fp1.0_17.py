import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("file::memory:?cache=shared")
import platform
import re
import os
import sys
import time
import traceback
import random
import string

from . import util

try:
    from . import _sqlite
except ImportError:
    _sqlite = None

try:
    from . import _sqlite3_ctypes
except ImportError:
    _sqlite3_ctypes = None

try:
    from . import _sqlite3_cffi
except ImportError:
    _sqlite3_cffi = None

try:
    from . import _sqlite3_ctypes_wrap
except ImportError:
    _sqlite3_ctypes_wrap = None


def _get_cached_sqlite3_dll():
    global _cached_sqlite3_dll
    if _cached_sqlite3_dll is None:
        _cached_sqlite3_dll = _get_sqlite3_dll()
