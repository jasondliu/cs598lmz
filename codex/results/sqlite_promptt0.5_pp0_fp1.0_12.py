import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared', uri=True)

import time
import random

# REFERENCE: https://github.com/python/cpython/blob/master/Modules/_ctypes/libffi/src/x86/ffitarget.h

# from ctypes import *
# from ctypes.util import find_library
# import _ctypes
# import ctypes.util
#
# libc = CDLL(find_library("c"))
# libc.printf(b"Hello %s!\n", b"world")
#
#
# libc = CDLL(find_library("c"))
# print(libc.printf(b"Hello %s!\n", b"world"))
#
#
# libc = CDLL(find_library("c"))
# print(libc.printf(b"Hello %s!\n", b"world"))
#
#
# libc = CDLL(find_library("c"))
# print(libc.printf(b"Hello %s!\n", b"world"))
#
