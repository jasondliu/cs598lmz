import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# this is a function pointer type
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

restype = ctypes.c_int
argtypes = (ctypes.c_int,)

# this is a function pointer
f = prototype(("._testfunc_i_i", lib), argtypes)

# this is a function pointer too
f = prototype(("._testfunc_i_i", lib), argtypes)

# this is a function pointer too
f = prototype(("._testfunc_i_i", lib), argtypes)

# this is a function pointer too
f = prototype(("._testfunc_i_i", lib), argtypes)

# this is a function pointer too
f = prototype(("._testfunc_i_i", lib), argtypes)

# this is a function pointer too
f = prototype(("._testfunc_i_i", lib), argtypes)

#
