import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memory:?cache=shared', uri=True)

import logging
logger = logging.getLogger(__name__)

from . import _sqlite3

__all__ = ['Connection', 'Row', 'register_adapter', 'register_converter',
           'complete_statement', 'enable_callback_tracebacks',
           'enable_shared_cache', 'PARSE_COLNAMES', 'PARSE_DECLTYPES',
           'PARSE_DECLTYPES']

PARSE_COLNAMES = _sqlite3.PARSE_COLNAMES
PARSE_DECLTYPES = _sqlite3.PARSE_DECLTYPES
PARSE_COLNAMES = _sqlite3.PARSE_COLNAMES

def enable_callback_tracebacks(flag):
    """Enable or disable callback functions throwing exceptions.

    If flag is True, any exception raised in a callback function will be
    re-raised in the main thread.
    """
    _sqlite3.enable_callback_tracebacks(flag)

def enable
