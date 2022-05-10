import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
# Test sqlite3.connect("file::memory:?cache=shared")

try:
    import resource
except ImportError:
    resource = None

try:
    import gc
except ImportError:
    gc = None

try:
    import sys
    sys.setcheckinterval(sys.getcheckinterval() * 10)
except (AttributeError, ImportError):
    pass

# Some tests on Windows fail if the disk is full.
# This is a problem with the Windows test runner, not with the tests.
# The Windows test runner should be fixed, but in the meantime,
# this code makes the tests runnable on a full disk.
try:
    import ctypes
except ImportError:
    ctypes = None
if ctypes:
    kernel32 = ctypes.windll.kernel32
    kernel32.SetErrorMode(1) # SEM_FAILCRITICALERRORS

# Disable the garbage collector if it exists.
if gc:
    gc.disable()

# Disable the sqlite3 module cache.
sql
