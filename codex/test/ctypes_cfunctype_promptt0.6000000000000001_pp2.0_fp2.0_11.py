import ctypes
# Test ctypes.CFUNCTYPE(None)
func = ctypes.CFUNCTYPE(None)(lambda: None)
func()

# Test ctypes.CFUNCTYPE(c_int)
