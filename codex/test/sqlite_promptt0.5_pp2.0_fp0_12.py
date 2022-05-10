import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('file:memory:?cache=shared')
import os
import sys
import unittest
from test import support
from test.support import import_fresh_module, forget, is_jython, is_android
import weakref
import gc

# Skip test if the _sqlite module wasn't built.
support.import_module('_sqlite3')

# Skip tests if the _sqlite module is built without the SQLITE_OMIT_LOAD_EXTENSION
# option.
support.requires('sqlite_omit_load_extension',
                 'test requires sqlite_omit_load_extension')

# Skip tests if the _sqlite module is built without the SQLITE_OMIT_LOAD_EXTENSION
# option.
support.requires('sqlite_omit_load_extension',
                 'test requires sqlite_omit_load_extension')

# Skip tests if the _sqlite module is built without the SQLITE_OMIT_LOAD_EXTENSION
# option.
