import ctypes
# Test ctypes.CFUNCTYPE type

import ctypes as C

# Simple callback
CB_FUNC = C.CFUNCTYPE(C.c_int, C.POINTER(C.c_int))

