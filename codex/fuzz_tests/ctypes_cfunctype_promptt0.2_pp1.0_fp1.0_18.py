import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function pointer type.
# It takes an integer argument, and returns an integer.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is a function pointer type.
# It takes an integer argument, and returns a pointer to a function
# pointer.
FUNC2 = ctypes.CFUNCTYPE(FUNC, ctypes.c_int)

# This is a function pointer type.
# It takes an integer argument, and returns a pointer to a function
# pointer.
FUNC3 = ctypes.CFUNCTYPE(FUNC2, ctypes.c_int)

# This is a function pointer type.
# It takes an integer argument, and returns a pointer to a function
# pointer.
FUNC4 = ctypes.CFUNCTYPE(FUNC3, ctypes.c_int)

# This is a function pointer type.
# It takes an integer argument
