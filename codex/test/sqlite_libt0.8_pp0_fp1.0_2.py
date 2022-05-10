import ctypes
import ctypes.util
import threading
import sqlite3
import time

from . import _ll2ctypes
from . import _cffi
from .. import _posixsubprocess

_cffi_backend = _cffi.get_backend()
ffi = _cffi_backend.ffi
libc = _cffi_backend.lib


# Error-checking versions of C lib funcs
def c_realloc(p, size):
    if p:
        p = ffi.gc(p, libc.free)

    if size:
        ptr = libc.realloc(p, size)
        if not ptr:
            raise MemoryError()
        p = ffi.gc(ptr, libc.free)
    else:
        ptr = 0
    return ptr

def c_malloc(size):
    ptr = libc.malloc(size)
    if not ptr:
        raise MemoryError()
    return ffi.gc(ptr, libc.free)


# Check for the availability of functions in the C library
