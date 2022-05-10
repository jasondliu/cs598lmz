import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import inspect
import signal
import time
import traceback
import logging

__version__ = '0.9.1'

class Error(Exception):
    pass

class InvalidConnection(Error):
    pass

class InvalidCursor(Error):
    pass

class Warning(Exception):
    pass

class InterfaceError(Error):
    pass

class DatabaseError(Error):
    pass

class InternalError(DatabaseError):
    pass

class OperationalError(DatabaseError):
    pass

class ProgrammingError(DatabaseError):
    pass

class IntegrityError(DatabaseError):
    pass

class DataError(DatabaseError):
    pass

class NotSupportedError(DatabaseError):
    pass

class ModuleNotFoundError(ImportError, LookupError):
    pass

class ArgumentError(TypeError):
    pass

def register_adapters_and_converters():
    def adapt_date(val):
        return val.isoformat()
    def convert_date(val):
        return datetime.date(*map(int
