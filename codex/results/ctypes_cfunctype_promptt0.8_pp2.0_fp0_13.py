import ctypes
# Test ctypes.CFUNCTYPE.

# test c_double, c_float, c_int, c_long
assert ctypes.CFUNCTYPE(c_double)(lambda x: x*2)(2.0) == 4.0
assert ctypes.CFUNCTYPE(c_float)(lambda x: x*2)(2.0) == 4.0
assert ctypes.CFUNCTYPE(c_int)(lambda x: x*2)(2) == 4
assert ctypes.CFUNCTYPE(c_long)(lambda x: x*2)(2) == 4

# test c_short
assert ctypes.CFUNCTYPE(c_short)(lambda x: x*2)(2) == 4
assert ctypes.CFUNCTYPE(c_short)(lambda x: x*2)(-2) == -4

# test c_longlong
assert ctypes.CFUNCTYPE(c_longlong)(lambda x: x*2)(2) == 4
assert ctypes.CFUNCTYPE(c_longlong)(lambda x: x*2)(-2) ==
