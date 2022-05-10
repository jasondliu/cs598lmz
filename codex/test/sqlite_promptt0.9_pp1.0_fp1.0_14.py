import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection.Connection
from _test import dbapi
import weakref

import cPickle
from test import test_support
import unittest

# silence deprecation warnings under py3k
try:
    import warnings
    warnings.filterwarnings("ignore", "the sets module is deprecated",
                            DeprecationWarning,
                            r"^test(test_support)?\.py$")
except (AttributeError, ImportError):
    pass

test_support.requires("network")
if test_support.is_jython:
    test_support.requires("audio")

if test_support.is_resource_enabled('audio'):
    try:
        import sunaudio
        have_sunaudio = 1
    except ImportError:
        have_sunaudio = 0

HAVE_WITH = False
HAVE_EXPAT = False

try:
    exec ("with open('') as f:\n    pass\n")
    HAVE_WITH = True
except SyntaxError:
    pass

