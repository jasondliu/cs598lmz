import ctypes
import ctypes.util
import threading
import sqlite3
import re
import json
import os
import os.path
import sys

# python2.6 compatibility
try:
    import simplejson as json
except ImportError:
    pass

# python3 compatibility
try:
    xrange
except NameError:
    xrange = range

# sqlite3.Row is not an iterator in python2.6.
# Fix that.
if sys.version_info[:2] == (2, 6):
    def iteritems(d):
        return d.iteritems()
    def iterkeys(d):
        return d.iterkeys()
    def itervalues(d):
        return d.itervalues()
    sqlite3.Row.__iter__ = lambda self: iterkeys(self)
else:
    iteritems = lambda d: iter(d.items())
    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())

# https://github.com/mozilla/gecko-dev/blob/master/xpcom/base/nsDebug
