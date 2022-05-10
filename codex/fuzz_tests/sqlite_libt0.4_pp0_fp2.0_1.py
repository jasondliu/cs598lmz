import ctypes
import ctypes.util
import threading
import sqlite3
import time

# libm.so.6 is the math library on Linux
# libm.dylib is the math library on OS X
# Note: The following line may need to be edited for your system
# since the name and location of this library file may be different
_libm = ctypes.CDLL(ctypes.util.find_library("m"))

# These are the function prototypes for the simple C functions
# that we want to call.  Notice that they match the definitions
# in the C code above.
_sin = _libm.sin
_sin.argtypes = [ctypes.c_double]
_sin.restype = ctypes.c_double

_cos = _libm.cos
_cos.argtypes = [ctypes.c_double]
_cos.restype = ctypes.c_double

_tan = _libm.tan
_tan.argtypes = [ctypes.c_double]
_tan.restype = ctypes.c_double

_pow = _libm.pow
_pow.argtypes = [ctypes.
