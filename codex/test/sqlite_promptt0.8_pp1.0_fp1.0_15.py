import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import os
import pathlib
import pytest

# Helper for testing

def has_sqlite(usethread=True):
    """Check if a sqlite module can be found"""
    try:
        sqlite3
    except NameError:
        return False
    fname = ctypes.util.find_library('sqlite3')
    if usethread:
        # check initialization of sqlite3
        try:
            with sqlite3.connect(':memory:'):
                pass
        except:
            return False
        # check thread safety
        try:
            sqlite3.threadsafety
        except AttributeError:
            return False
        if sqlite3.threadsafety < 2:
            return False
        # check for ctypes
        try:
            ctypes
        except NameError:
            return False
        # check that we can load a shared library
        try:
            handle = ctypes.CDLL(fname)
        except OSError:
            pass
