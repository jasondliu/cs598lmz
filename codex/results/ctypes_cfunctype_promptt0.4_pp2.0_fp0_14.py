import ctypes
# Test ctypes.CFUNCTYPE()

# NOTE: ctypes.CFUNCTYPE() is not supported on Windows.

import ctypes

# This function takes a function pointer as an argument.
def func(f, arg):
    return f(arg)

# This function is passed as an argument to func().
def callback(arg):
    return arg

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Create the function pointer.
cmp_func = CMPFUNC(callback)

# Call the function.
print func(cmp_func, 1)

# Test ctypes.POINTER()

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

# Create a pointer to POINT.
point_ptr = ctypes.POINTER(POINT)

# Create an instance of POINT.
point = POINT(1, 2)

# Cast the instance to a pointer.

