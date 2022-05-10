import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import time
import re
import socket
import sys
import logging

# No threading import in Python3
if sys.version_info.major == 2:
    from threading import _Timer
else:
    from threading import Timer as _Timer

# Python3 does not have a next() function any more
if sys.version_info.major == 3:
    next = lambda x: x.__next__()

# Python 2.6 does not have a with statement
try:
    import __builtin__
    exec('from __builtin__ import with_statement')
except ImportError:
    def with_statement():
        return lambda x: x

# Timeout class with Python3 compatibility
class Timeout(_Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        _Timer.__init__(self, interval, function, args, kwargs)

    def run(self):
        while True:
            self.finished.wait(self.interval)
