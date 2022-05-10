import ctypes
# Test ctypes.CFUNCTYPE
assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double) is ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)
assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double) is not ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
assert ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double) is not ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Test ctypes.PYFUNCTYPE
assert ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_double) is ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_double)
assert ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_double) is not ctypes.PYFUNCTYPE(ctypes.c
