import ctypes
# Test ctypes.CFUNCTYPE()
#
# Demonstrates how to create a ctypes callback function, and how to
# create a ctypes callback function pointer.
#
# See:
#  http://docs.python.org/library/ctypes.html#ctypes._FuncPtr
#  http://docs.python.org/library/ctypes.html#ctypes.CFUNCTYPE
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
from ctypes import *

# A simple callback function
def py_callback(x, y):
    print('Hello from Python callback function!')
    print('x={}, y={}'.format(x, y))
    return x + y

# Define the return type and argument types of the callback
# function that will be passed to C
cb_type = CFUNCTYPE(c_int, c_int, c_int)

# Create a pointer to the callback function
cb_func = cb_type(py_callback)

# Declare a C function (with a C callback pointer parameter)
