import ctypes
import ctypes.util
import threading
import sqlite3
import os.path
import sys
import logging
import time
import re

from . import resources

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

def _check_errno(result, func, args):
    if result < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return result

libc.open.errcheck = _check_errno
libc.open.argtypes = [ctypes.c_char_p, ctypes.c_int]
libc.open.restype = ctypes.c_int

libc.close.errcheck = _check_errno
libc.close.argtypes = [ctypes.c_int]
libc.close.restype = ctypes.c_int

libc.read.errcheck = _check_errno
libc.read.argtypes = [ctypes.c_int, ctypes.c_void_p,
