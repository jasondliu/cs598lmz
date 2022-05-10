import ctypes
import ctypes.util
import threading
import sqlite3

import numpy as np

######################### Private helper functions #########################
# these use a setup which is common to all functions
# in the public API.

_MULTI_THREADED = ctypes.c_int.in_dll(
    ctypes.CDLL(ctypes.util.find_library('libsqlite3')),
    'sqlite3_threadsafe'
)

def _access_ctypes_result(result, func, cargs):
    rv = ctypes.pythonapi.PyEval_CallObject(func, cargs)
    ctypes.pythonapi.Py_DecRef(cargs)
    if rv == 0:
        raise sqlite3.DatabaseError()
    return result.value

def singleton(cls):
    '''Transforms `cls` into a singleton.
    '''
    instances = {}
