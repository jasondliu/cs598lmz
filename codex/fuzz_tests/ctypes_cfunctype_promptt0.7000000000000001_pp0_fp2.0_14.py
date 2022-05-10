import ctypes
# Test ctypes.CFUNCTYPE

# In this test, we test that you can create a ctypes.CFUNCTYPE
# instance that takes more than one argument and returns a
# ctypes instance.

from ctypes import *

import unittest
from test import support

################################################################

# /usr/include/unistd.h:
#
# extern ssize_t write(int fildes, const void *buf, size_t nbyte);
#
# Python equivalent:

_write = CFUNCTYPE(c_ssize_t, c_int, c_void_p, c_ulong)(("write", libc))
_write.restype = c_ssize_t
_write.argtypes = (c_int, c_void_p, c_ulong)

def write(fd, buf, n):
    return _write(fd, buf, n)

class TestCFuncPtr(unittest.TestCase):
    def test_write(self):
        from io import BytesIO
        f = BytesIO()

        fd = f
