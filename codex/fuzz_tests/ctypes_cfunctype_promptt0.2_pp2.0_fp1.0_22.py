import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function that takes a function pointer as argument
# and calls it
lib.call_function.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
lib.call_function.restype = ctypes.c_int

# a function that takes a function pointer as argument
# and returns it
lib.return_function.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
lib.return_function.restype = ctypes.c_void_p

# a function that takes a function pointer as argument
# and returns it
lib.return_function_as_int.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
lib.return_function_as_int.restype = ctypes.c_int

# a function that takes a function pointer as argument
# and returns it
lib.
