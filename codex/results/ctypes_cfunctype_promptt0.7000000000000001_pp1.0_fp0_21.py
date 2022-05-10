import ctypes
# Test ctypes.CFUNCTYPE()

def func(x, y):
    return x * 2 + y * 2

def func_ptr(x, y):
    return func(x, y)

# CFUNCTYPE is a standard ctypes type for C functions.
# It usually takes the signature, and returns a type object.
CFuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The CFuncType type object can then be used as a normal type specifier.
c_func = CFuncType(func_ptr)

# Use it like a normal Python function:
print(c_func(2, 3))
# Output: 10

# We can also do this all in one step:
c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(func)

# This is a mainstay of ctypes-based Python-C interoperation.
# It's important to understand that the function and the function pointer
# are not the
