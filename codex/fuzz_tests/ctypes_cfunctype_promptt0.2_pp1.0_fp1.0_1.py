import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The CFUNCTYPE factory function creates a type that can be used
# to create C callable function pointers.
#
# The first argument is the return type, the next arguments are the
# argument types.
#
# The callable instances created from this type call the C function
# specified when the instance is created.

# The prototype of the C function is:
#
#   int function(int, int)

CFunctionType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Create an instance of the C function type
# The first argument is the name of the C function in the shared
# library, the rest of the arguments are passed to the constructor
# of the function type.

CFunction = CFunctionType(("function", lib), (1, "spam"))

# The function can now be called

print(CFunction(2, 3))

# The function can
