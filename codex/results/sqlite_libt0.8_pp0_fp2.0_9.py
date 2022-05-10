import ctypes
import ctypes.util
import threading
import sqlite3
import sys

if sys.version_info[:2] == (2, 6):
    import unittest2 as unittest
else:
    import unittest

from nose.plugins.skip import SkipTest

from sqlite3 import dbapi2 as sqlite

libsqlite = ctypes.CDLL(ctypes.util.find_library('sqlite3'))

def make_definition(name, restype, *argtypes):
    getattr(libsqlite, name).restype = restype
    getattr(libsqlite, name).argtypes = argtypes

make_definition('sqlite3_enable_shared_cache', ctypes.c_int, ctypes.c_int)

SQLITE_OPEN_READONLY = 0x00000001
SQLITE_OPEN_READWRITE = 0x00000002
SQLITE_OPEN_CREATE = 0x00000004
SQLITE_OPEN_DELETEONCLOSE = 0x00000008
SQLITE_OPEN_EXCLUSIVE = 0x00000010
SQLITE_OPEN_AUTOP
