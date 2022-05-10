import ctypes
# Test ctypes.CFUNCTYPE
def callback(x):
    return x
cb = ctypes.CFUNCTYPE(ctypes.c_int)(callback)
assert cb(42) == 42

# Test ctypes.CFUNCTYPE with calling convention
def callback(x):
    return x
cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, calling_convention='win64')(callback)
assert cb(42) == 42

# Test ctypes.CFUNCTYPE with complex
def callback(x):
    return x
cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_complex)(callback)
assert cb(42) == 42

# Test ctypes.CFUNCTYPE with void*
def callback(x):
    return x
cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)(callback)
assert cb(42) == 42

# Test ctypes.CFUNCTYPE with object
def callback(x
