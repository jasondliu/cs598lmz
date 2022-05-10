import ctypes
import ctypes.util
import threading
import sqlite3
import traceback
import re
import operator
import inspect

# Bindings to the C library libcouchbase
# Configure the path to the library if you need to
_lcb_lib = ctypes.CDLL(ctypes.util.find_library('couchbase'))

# The default path to the library, if found on the system
default_path = None


class Error(Exception):
    """
    Base class for all exceptions
    """
    def __init__(self, rc=None, obj=None, msg=None):
        self.rc = rc
        self.obj = obj
        self.msg = msg

    def __str__(self):
        return self.msg


class AuthError(Error):
    """Exception for invalid credentials"""
    pass


class TimeoutError(Error):
    """Exception for timeouts"""
    pass


class ConnectError(Error):
    """Exception for failed connection attempts"""
    pass


class ObjectTemporaryFailError(Error):
    """Thrown when the operation would succeed but is temporarily disabled"""
    pass


class
