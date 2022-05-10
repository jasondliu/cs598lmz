import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import os
import sys
import time

from . import _sqlite3
from . import _testcapi

try:
    import gc
except ImportError:
    gc = None

try:
    import _testinternalcapi
except ImportError:
    _testinternalcapi = None

# Silence Py3k warning
if sys.py3kwarning:
    import warnings
    warnings.filterwarnings("ignore", ".*mimetools has been removed",
                            DeprecationWarning)
    warnings.filterwarnings("ignore", ".*string or file", DeprecationWarning)

# ----------------------------------------------------------------------
# OPTIONS

verbose = False

# ----------------------------------------------------------------------
# UTILITIES

def uniq(seq):
    seen = set()
    return [x for x in seq if x not in seen and not seen.add(x)]

def verify(condition, message):
    if not condition:
        raise Exception(message)

