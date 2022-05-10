import ctypes
# Test ctypes.CFUNCTYPE(None)
func = ctypes.CFUNCTYPE(None)(lambda: None)
func()

# Test ctypes.CFUNCTYPE(c_int)
func = ctypes.CFUNCTYPE(c_int)(lambda: 42)
assert func() == 42

# Test ctypes.CFUNCTYPE(c_int, c_int)
func = ctypes.CFUNCTYPE(c_int, c_int)(lambda x: x * 2)
assert func(21) == 42

# Test ctypes.CFUNCTYPE(c_int, POINTER(c_int))
func = ctypes.CFUNCTYPE(c_int, POINTER(c_int))(lambda p: p[0])
x = c_int(42)
assert func(x) == 42

# Test ctypes.CFUNCTYPE(c_int, POINTER(c_int), c_int)
func = ctypes.CFUNCTYPE(c_int, POINTER(c_int), c_int)(lambda p, x:
