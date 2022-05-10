import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import _sqlite3

try:
    from _testcapi import getargs_keywords, getargs_b
except ImportError:
    def getargs_keywords(*args, **kwargs):
        return args, kwargs
    def getargs_b(*args, **kwargs):
        return args, kwargs

try:
    from _testcapi import getargs_keywords_only
except ImportError:
    def getargs_keywords_only(**kwargs):
        return kwargs

try:
    from _testcapi import getargs_keywords_w
except ImportError:
    def getargs_keywords_w(*args, **kwargs):
        return args, kwargs

try:
    from _testcapi import getargs_posonly
except ImportError:
    def getargs_posonly(*args):
        return args

