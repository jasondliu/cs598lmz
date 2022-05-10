import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("file:memdb1?mode=memory&cache=shared")

import unittest
import weakref
import gc

# Test the SQLite driver

from test import test_support

# Skip test if _sqlite is not built or sqlite is not available
test_support.import_module('_sqlite3')
test_support.import_module('sqlite3')

# This is used by the decorator to hold the original functions
FUNCTIONS = {}

def sqlite_version_prop(f):
    def getter(self):
        return f(self)
    return property(getter)

def decorate_all_tests(base_class, sqlite_version=None):
    """Decorate all tests to skip if sqlite version is not sufficient."""
    for name in base_class.__dict__:
        if name.startswith("test_"):
            test = getattr(base_class, name)
            if not hasattr(test, "__call__"):
                continue
