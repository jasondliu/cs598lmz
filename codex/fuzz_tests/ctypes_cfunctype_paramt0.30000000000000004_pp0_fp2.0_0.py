import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def cb(a, b):
    print a, b
    return a + b
cb_func = FUNTYPE(cb)

# Create a new function object
f = Function(cb_func)

# Call the function
print f(1, 2)

# Create a new function object
f = Function(cb_func, [int, int], int)

# Call the function
print f(1, 2)

# Create a new function object
f = Function(cb_func, [int, int], int, error_policy=THROW_ERROR)

# Call the function
print f(1, 2)

# Create a new function object
f = Function(cb_func, [int, int], int, error_policy=THROW_ERROR, calling_convention=CALL_BY_VALUE)

# Call the function
print f(1, 2)

# Create a new function object
f = Function(cb_func, [int, int], int, error_
