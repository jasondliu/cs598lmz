import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# A function taking no arguments and returning an integer
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int)

# A function taking two integers and returning an integer
CMPFUNC2 = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# A function taking no arguments and returning void
VOIDFUNC = ctypes.CFUNCTYPE(None)

# A function taking two integers and returning void
VOIDFUNC2 = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# A function taking a pointer to a function taking no arguments and returning
# void, and returning void
VOIDFUNC3 = ctypes.CFUNCTYPE(None, VOIDFUNC)

# A function taking a pointer to a function taking no arguments and returning
# void,
