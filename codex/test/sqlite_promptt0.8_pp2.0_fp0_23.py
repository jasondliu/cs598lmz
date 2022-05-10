import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import sys, os
import logging
import itertools as it

if sys.version_info < (3, ):
    range = xrange

#
# Define the SQLite library interface
#
_lib = ctypes.util.find_library('sqlite3')
_lib = ctypes.CDLL(_lib)
