import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

# This is a work-around for a bug in the 2.5.2 version of Python, where the
#  ctypes implementation of get_errno() is broken.  It is fixed in Python 2.6.
#  This code is borrowed from the ctypes SVN repository.
_errno = ctypes.CDLL(ctypes.util.find_library("c"), use_errno=True)
if hasattr(_errno, '__errno_location'):
    _errno_location = _errno.__errno_location
elif os.name == "nt":
    _errno_location = lambda: ctypes.byref(ctypes.c_int.in_dll(_errno, '_doserrno'))
else:
    _errno_location = lambda: ctypes.byref(ctypes.c_int.in_dll(_errno, 'errno'))
def get_errno():
    errno = _errno_location().contents.value
    return errno

