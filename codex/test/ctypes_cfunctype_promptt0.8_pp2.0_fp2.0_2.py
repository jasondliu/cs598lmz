import ctypes
# Test ctypes.CFUNCTYPE
cf = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
f = cf((lambda x: 127))
assert f(42) == 127
# Test ctypes.byref()
l = ctypes.c_long(1)
