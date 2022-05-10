import ctypes
# Test ctypes.CFUNCTYPE()
def func(a, b):
    return a + b

# Create a C function pointer from Python function
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

# Call C function pointer
print(cfunc(1, 2))

# Create a C function pointer from Python function
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

# Call C function pointer
print(cfunc(1, 2))

# Create a C function pointer from Python function
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

# Call C function pointer
print(cfunc(1, 2))

# Create a C function pointer from Python function
cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

