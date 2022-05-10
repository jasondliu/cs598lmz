import ctypes
# Test ctypes.CFUNCTYPE
def func(a, b):
    return a + b

# The first argument is the return type, the rest are the argument types.
# The rest of the arguments to create_function are the same as those to
# CFUNCTYPE.
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convert func using the CMPFUNC function prototype.
cmp_func = CMPFUNC(func)

# Call cmp_func.
print(cmp_func(1, 2))

# Test ctypes.PYFUNCTYPE
# The first argument is the return type, the rest are the argument types.
# The rest of the arguments to create_function are the same as those to
# PYFUNCTYPE.
PYFUNC = ctypes.PYFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)

# Convert func using the PYFUNC function prototype.
py_func = PYFUNC
