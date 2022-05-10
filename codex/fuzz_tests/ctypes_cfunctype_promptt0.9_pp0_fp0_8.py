import ctypes
# Test ctypes.CFUNCTYPE(None)
ptype = ctypes.CFUNCTYPE(None)
ptype.__name__

# Test ctypes.CFUNCTYPE(None, None)
ptype = ctypes.CFUNCTYPE(None, None)
ptype.__name__

# Test ctypes.CFUNCTYPE(None, c_int)
ptype = ctypes.CFUNCTYPE(None, c_int)
ptype.__name__

# Test ctypes.CFUNCTYPE(c_int, c_int, c_int)
ptype = ctypes.CFUNCTYPE(c_int, c_int, c_int)
ptype.__name__

# Test overloaded function
ptype = ctypes.CFUNCTYPE(None, c_int)
ptype.__name__
ptype = ctypes.CFUNCTYPE(None, c_double)
ptype.__name__

# Test callbacks with string argument
ptype = ctypes.CFUNCTYPE(None, c_char_p
