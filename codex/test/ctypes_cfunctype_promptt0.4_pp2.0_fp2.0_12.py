import ctypes
# Test ctypes.CFUNCTYPE

def test_func(a, b):
    return a + b

# This is a function pointer
CFuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convert the Python function into C function pointer.
cfunc = CFuncPtr(test_func)

# Call the C function pointer to execute the Python function.
print(cfunc(1, 2))

# Test ctypes.PYFUNCTYPE

def test_func(a, b):
    return a + b

# This is a function pointer
PFuncPtr = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convert the Python function into C function pointer.
cfunc = PFuncPtr(test_func)

# Call the C function pointer to execute the Python function.
print(cfunc(1, 2))

# Test ctypes.WINFUNCTYPE

