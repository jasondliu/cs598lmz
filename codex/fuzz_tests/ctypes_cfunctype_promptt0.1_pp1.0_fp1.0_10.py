import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

# the function pointer type is defined in the C source file
# as:
#   int (*func)(int)

# the Python callable is a function which takes an integer
# argument and returns an integer

# the C function is called with the Python callable as
# argument, and returns the result of calling the callable

# the C function is called with the integer 42 as argument
# the Python callable returns the argument + 1
# the C function returns the result of calling the callable
# which is 43

# the C function is called with the integer -1 as argument
# the Python callable returns the argument + 1
# the C function returns the result of calling the callable
# which is 0

# the C function is called with the integer -2 as argument
# the Python callable returns the argument + 1
# the C function returns the result of calling the callable
# which is -
