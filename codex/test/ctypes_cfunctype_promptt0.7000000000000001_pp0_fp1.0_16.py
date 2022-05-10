import ctypes
# Test ctypes.CFUNCTYPE

try:
    ctypes.CFUNCTYPE
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

import _ctypes

c_int_p = ctypes.POINTER(ctypes.c_int)
print(ctypes.CFUNCTYPE(c_int_p, c_int_p))

c_int_p = ctypes.POINTER(ctypes.c_int)
print(ctypes.CFUNCTYPE(ctypes.c_int, c_int_p))

c_int_p = ctypes.POINTER(ctypes.c_int)
print(ctypes.CFUNCTYPE(None, c_int_p))

c_int_p = ctypes.POINTER(ctypes.c_int)
print(ctypes.CFUNCTYPE(ctypes.c_int, c_int_p, c_int_p))

# Return type can be anything except function pointer
