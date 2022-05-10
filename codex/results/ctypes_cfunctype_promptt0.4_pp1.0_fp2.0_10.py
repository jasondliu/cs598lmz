import ctypes
# Test ctypes.CFUNCTYPE

# Test ctypes.CFUNCTYPE(None)
# This is a special case, because ctypes.CFUNCTYPE(None) is the same
# as ctypes.CFUNCTYPE(ctypes.c_int)

f = ctypes.CFUNCTYPE(None)
assert f(1, 2, 3) == 0

f = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)
assert f(1, 2, 3) == 0

f = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int)
assert f(1, 2, 3) == 0

f = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
assert f(1, 2, 3, 4) == 0

f = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.
