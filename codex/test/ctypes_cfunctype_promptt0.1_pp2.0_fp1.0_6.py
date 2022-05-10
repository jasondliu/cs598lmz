import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

# the function pointer type is defined in the C source file
# as:
#   int (*func)(int)

# the Python callable is called with an integer argument
# and must return an integer

# the C function returns the sum of the return values of
# the Python callable and the integer argument

# the C function is called with an integer argument
# the return value is the sum of the return values of
# the Python callable and the integer argument

# the Python callable is called with the integer argument
# the return value is the sum of the return values of
# the Python callable and the integer argument

# the Python callable returns the sum of the return values of
# the Python callable and the integer argument

# the Python callable is called with the integer argument
# the return value is the sum of the return values of
# the Python callable and the integer argument

#
