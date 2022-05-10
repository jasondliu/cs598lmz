import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

# The first argument is the return type of the callback.
# The rest are the argument types.
# The first argument must be an integer or a pointer.
# The rest must be integers.
callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

print(callback(1, 2))

# Test ctypes.WINFUNCTYPE

# The first argument is the return type of the callback.
# The rest are the argument types.
# The first argument must be an integer or a pointer.
# The rest must be integers.
callback = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

print(callback(1, 2))

# Test ctypes.PYFUNCTYPE

# The first argument is the return type of the callback.
# The rest are the argument types.
# The first argument must be an integer or a pointer.

