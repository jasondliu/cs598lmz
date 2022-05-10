import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# ctypes.CFUNCTYPE(<restype>, <argtypes>)
# <restype> is a C data type, such as ctypes.c_int
# <argtypes> is a tuple of C data types, such as (ctypes.c_float, ctypes.c_float)

import ctypes
import math

libc = ctypes.CDLL(None)
fabs = libc.fabs
fabs.argtypes = (ctypes.c_double,)
fabs.restype = ctypes.c_double

fabs(-1.2)

ctypes.c_float(1.1).value
float.fromhex('0x1.1p+3')

libc.sin.argtypes = (ctypes.c_double,)
libc.sin.restype = ctypes.c_double

libc.sin(1.0)

ctypes.c_int.from_buffer(b'abc').value

ctypes.c_int.from_buffer(b'abc', 1).value

