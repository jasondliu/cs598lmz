import ctypes
import ctypes.util
import threading
import sqlite3
import pprint

from ctypes import *

import logging
logger = logging.getLogger(__name__)

#
# Define some constants
#

#
# Define some basic types
#

#
# Define some structures
#

#
# Define the API
#

class LibSqlite3(object):
    def __init__(self):
        self.cdll = None
        self.libc = None

        #
        # Import the C library
        #
        self.cdll = ctypes.CDLL(ctypes.util.find_library('sqlite3'), use_errno=True)
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

        #
        # Setup the return types and argument types
        #
        self.cdll.sqlite3_libversion.restype = c_char_p
        self.cdll.sqlite3_libversion_number.restype = c_int

        #
        # Define
