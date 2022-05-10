import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is the prototype of the callback function
# The callback function takes an integer and returns an integer
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the prototype of the function that takes a callback function
# as an argument
# The function takes a callback function and an integer and returns an integer
FUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, CALLBACKFUNC, ctypes.c_int)

# This is the prototype of the function that is implemented in C
# The function takes an integer and returns an integer
CFUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the prototype of the function that is implemented in C
# The function takes a callback function and an integer and returns an integer
CFUNCTYPE2 = ctypes.CFUNCTYPE(ctypes.c_int, CFUNCTYPE, ctypes.c_int)

# This is
