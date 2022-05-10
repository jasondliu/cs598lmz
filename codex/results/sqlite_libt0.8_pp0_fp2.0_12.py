import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import sys
import traceback

'''
    This is a stripped-down version of the python daemon and lockfile
    libraries.

    https://pypi.python.org/pypi/python-daemon/
    https://pypi.python.org/pypi/lockfile/

    The daemon version is compatible with Python 2 and 3,
    and has been stripped down to include only the absolute minimum.
'''

def _excepthook(excType, excValue, tracebackobj):
    sys.__excepthook__(excType, excValue, tracebackobj)

sys.excepthook = _excepthook

POSIX = os.name == 'posix'

# Exceptions

class DaemonOSEnvironmentError(Exception):
    """Raised when an operation on the daemon process's environment fails."""

class DaemonProcessDetachError(Exception):
    """Raised when a daemon process cannot detach from its controlling terminal."""

class DaemonContextError(Exception):
    """Raised when an
