import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys

# -- global varibales --

# DB related
db_path = None
conn = None
cursor = None

# exception-handling related
error_lst = {
    -1 : 'SQLITE_ERROR',
    -2 : 'SQLITE_INTERNAL',
    -3 : 'SQLITE_PERM',
    -4 : 'SQLITE_ABORT',
    -5 : 'SQLITE_BUSY',
    -6 : 'SQLITE_LOCKED',
    -7 : 'SQLITE_NOMEM',
    -8 : 'SQLITE_READONLY',
    -9 : 'SQLITE_INTERRUPT',
    -10 : 'SQLITE_IOERR',
    -11 : 'SQLITE_CORRUPT',
    -12 : 'SQLITE_NOTFOUND',
    -13 : 'SQLITE_FULL',
    -14 : 'SQLITE_CANTOPEN',
    -15 : 'SQLITE_PROTOCOL',
    -16 : 'SQLITE_EMPTY',

