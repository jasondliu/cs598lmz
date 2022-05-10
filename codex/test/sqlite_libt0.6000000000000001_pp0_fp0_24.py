import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import traceback
import inspect
import re

from . import _lib

class Error(Exception):
    pass

class UnsupportedOperation(Error):
    pass

class DataError(Error):
    pass

class DatabaseError(Error):
    pass

class OperationalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class InterfaceError(DatabaseError):
    pass

class InternalError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

# Map SQLite result codes to exceptions
