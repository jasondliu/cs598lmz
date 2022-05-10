import ctypes
# Test ctypes.CFUNCTYPE for functions with non-void return types.
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

#
# The following code is based on the ctypes tutorial by Thomas Heller
#

# Return a function pointer with the prototype int func(int)
FUNC_INT_INT = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The following is not yet supported by ctypes.
## FUNC_FLOAT_FLOAT = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

# Return an INT
prototype1 = ctypes.CFUNCTYPE(ctypes.c_int)
# Return a POINTER(c_int)
prototype2 = ctypes.CFUNCTYPE(ctypes.POINTER(ctypes.c_int))

# Return a function pointer with the prototype int func(int)
