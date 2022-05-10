import ctypes
# Test ctypes.CFUNCTYPE, ctypes.c_int and ctypes.c_int32, as well as
# POINTER(c_int)
if ctypes.sizeof(ctypes.c_int) == 4:
    c_int32 = ctypes.c_int
else:
    c_int32 = ctypes.c_int32

import operator

