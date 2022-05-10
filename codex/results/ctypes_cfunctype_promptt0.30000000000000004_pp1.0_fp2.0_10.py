import ctypes
# Test ctypes.CFUNCTYPE()

# This is a function that takes a function pointer as an argument.
# The function pointer takes an integer and returns an integer.

# The function pointer is passed as an argument to the function.
# The function calls the function pointer and returns the result.

# The function pointer is created using CFUNCTYPE.

import ctypes
from ctypes import *

# C code
# int callfunc(int (*func)(int), int arg) {
#     return func(arg);
# }

# Ctypes code

# int callfunc(int (*func)(int), int arg);

callfunc = cdll.msvcrt.callfunc
callfunc.argtypes = [CFUNCTYPE(c_int, c_int), c_int]
callfunc.restype = c_int

# int func(int);
func = CFUNCTYPE(c_int, c_int)(lambda i: i * 2)

assert callfunc(func, 5) == 10
