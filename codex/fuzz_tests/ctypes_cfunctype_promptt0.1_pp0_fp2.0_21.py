import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument
# the function pointer argument is a Python callable

# the function pointer type is defined in _ctypes_test
# as 'int (*func)(int)'

# the function to be called is 'int func(int)'

# the function pointer is passed as a keyword argument

# the function returns the value passed to the function pointer

# the function pointer is called with the value 42

# the function returns 42

# the function pointer is called with the value 17

# the function returns 17

# the function pointer is called with the value -1

# the function returns -1

# the function pointer is called with the value 0

# the function returns 0

# the function pointer is called with the value 1

# the function returns 1

# the function pointer is called with the value 2

# the function returns 2

# the function pointer is called with the value 3

# the function returns 3

# the function pointer
