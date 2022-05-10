import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int, ctypes.c_double and callback

from ctypes import CFUNCTYPE, c_int, c_double

SIMPLE_FUNC_PROTO = CFUNCTYPE(None)

