import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time

from ctypes import *

#
# This is a test for the Python ctypes module
#

#
# Load the shared library into ctypes
#

# The following works when the library is in the same directory as this file
#_test = ctypes.CDLL("./libtest.so")

# The following works when the library is in LD_LIBRARY_PATH
_test = ctypes.CDLL("libtest.so")

#
# Set up the return types and argument types for the functions we want to call
#

_test.test_int.restype = c_int
_test.test_int.argtypes = [c_int]

_test.test_string.restype = c_char_p
_test.test_string.argtypes = [c_char_p]

_test.test_string_length.restype = c_int
_test.test_string_length.argtypes = [c_char_p]

_test.test_string_length_const.restype
