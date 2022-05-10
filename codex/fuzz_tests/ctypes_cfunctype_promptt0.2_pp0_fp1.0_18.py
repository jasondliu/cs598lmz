import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function taking a function pointer as argument
# and calling it
lib.call_function.argtypes = ctypes.CFUNCTYPE(ctypes.c_int),

# a function taking a function pointer as argument
# and returning it
lib.return_function.restype = ctypes.CFUNCTYPE(ctypes.c_int)

# a function taking a function pointer as argument
# and returning it
lib.return_function_ex.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# a function taking a function pointer as argument
# and returning it
lib.return_function_ex2.restype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# a function taking a function pointer as argument
# and returning it
lib.return_function_ex3.restype = ctypes.CFUN
