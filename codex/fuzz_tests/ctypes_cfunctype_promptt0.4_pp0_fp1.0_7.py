import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function taking a function pointer as argument
# The function pointer takes a double and returns a double
# The function returns a function pointer

prototype = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
paramflags = (1, "func"),

func = lib.returns_function(prototype, paramflags)

# func is a function pointer, call it

print(func(3.0))

# The function returned by lib.returns_function() is a function
# pointer, so we can pass it to another function taking a function
# pointer as argument.

lib.call_function(func)

# The function returned by lib.returns_function() is a function
# pointer, so we can pass it to another function taking a function
# pointer as argument.

lib.call_function(func)

# The function returned by lib.returns_function() is a function
# pointer, so we can pass
