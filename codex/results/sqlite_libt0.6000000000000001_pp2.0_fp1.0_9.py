import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys


_libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)

def _errcheck(result, func, args):
    if result < 0:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return result

_libc.prctl.argtypes = [ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong]
_libc.prctl.errcheck = _errcheck

PR_SET_NAME = 15
PR_GET_NAME = 16

def get_thread_name():
    """
    Returns the name of the current thread.
    """
    name = ctypes.create_string_buffer(16)
    length = _libc.prctl(PR_GET_NAME, ctypes.byref(name), 0, 0, 0)
    return name.value[:
