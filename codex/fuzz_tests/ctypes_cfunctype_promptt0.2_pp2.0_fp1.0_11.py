import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The CFUNCTYPE() constructor creates a C callable function from a Python
# callable object.
# The first argument is the return type, the default is c_int.
# The rest of the arguments are the argument types.

# The prototype of the function is:
# int func(int, int)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The Python function to call.
def py_func(a, b):
    print("py_func", a, b)
    return a + b

# Convert the Python function to a C callable function.
c_func = prototype(py_func)

# Call the C function.
res = lib.test_callfunc(c_func)
print(res)

# The CFUNCTYPE() constructor creates a C callable function from a Python
# callable object.
# The first argument
