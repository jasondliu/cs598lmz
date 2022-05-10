import ctypes
# Test ctypes.CFUNCTYPE
# The first argument of CFUNCTYPE is the return type.
# The rest are the argument types.
# The types are Python types and they are converted to C types when the
# function is called.

# Here's a simple example:
def py_func(a, b):
    return a + b

# Convert the Python function to a C function
c_func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(py_func)

# Call the C function.
print(c_func(1, 2))

# This is a bit silly, but it demonstrates that the C function calls the
# Python function.

# What happens when we pass the wrong types?
try:
    c_func(1.1, 2)
except TypeError as e:
    print(e)

try:
    c_func(1, 2.2)
except TypeError as e:
    print(e)

# What happens when we pass the wrong number of arguments?
try:
    c_func
