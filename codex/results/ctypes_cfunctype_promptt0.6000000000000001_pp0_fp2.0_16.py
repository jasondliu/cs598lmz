import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Load the shared library into ctypes.
lib = ctypes.CDLL('./foo.so')

# Set up the return type and argument types.
lib.foo.restype = ctypes.c_int
lib.foo.argtypes = (ctypes.c_int, ctypes.c_int)

# Call the function, and print the result.
print(lib.foo(1, 2))

# Test ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# Load the shared library into ctypes.
lib = ctypes.CDLL('./foo.so')

# Set up the return type and argument types.
lib.foo.restype = None
lib.foo.argtypes = (ctypes.c_int, ctypes.c_int)

# Call the function, and print the result.
lib.foo(1, 2)
</code>

