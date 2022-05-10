import ctypes
# Test ctypes.CField

from ctypes import *
from ctypes.test import need_symbol

class X(Structure):
    _fields_ = [("a", c_int)]

class Y(Structure):
    _fields_ = [("b", c_int)]

cffe = CFUNCTYPE(None, POINTER(X))

def ptr_callback(ptr):
    assert ptr.contents.a == 111
    print('correct')

libc = None

try:
    if sizeof(c_void_p) == 4:
        libc = CDLL('msvcrt')
    else:
        libc = CDLL('msvcr100')
except OSError:
    try:
        libc = CDLL('libc.so.6')
    except OSError:
        pass
if not libc:
    raise Exception('no libc')

f = libc.memset
f.restype = c_void_p
f.argtypes = c_void_p, c_int, c_size_t

f
