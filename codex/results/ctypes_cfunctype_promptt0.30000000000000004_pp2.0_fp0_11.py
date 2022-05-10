import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    print a, b

# Create a C function pointer
c_func = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)

# Call the C function pointer
c_func(1, 2)

# Create a C function pointer with error checking
c_func = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int,
                          restype=ctypes.c_int,
                          errcheck=lambda result, func, arguments: None)(func)

# Call the C function pointer
c_func(1, 2)

# Create a C function pointer with error checking
c_func = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int,
                          restype=ctypes.c_int,
                          errcheck=lambda result, func, arguments: None)(func)

# Call the C function pointer
c_func(1, 2)

# Create a C function pointer
