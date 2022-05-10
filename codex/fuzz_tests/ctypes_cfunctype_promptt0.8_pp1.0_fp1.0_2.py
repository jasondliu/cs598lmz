import ctypes
# Test ctypes.CFUNCTYPE
#

import support

with support.ErrorHandling():
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, argtypes=(ctypes.c_int,))
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, restype=ctypes.c_int)
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, paramflags=(None, None, 1))
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, paramflags=(None, None, 1, 0))
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, paramflags=(None, None, 1, 0, 1))
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, paramflags=(None
