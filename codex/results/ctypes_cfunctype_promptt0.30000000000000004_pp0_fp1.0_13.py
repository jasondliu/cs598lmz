import ctypes
# Test ctypes.CFUNCTYPE

# This test is for the case where the function is called with a
# different number of arguments than the number of arguments in the
# prototype.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This function takes two arguments, but we call it with one
# argument.  The second argument is passed as a default parameter.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The second argument is passed as a default parameter.
f = prototype((("test_fn_callback", lib), (1,), None))

res = f(42)
if res != 42:
    raise RuntimeError("wrong result")

# This function takes two arguments, but we call it with one
# argument.  The second argument is passed as a default parameter.

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The second argument is passed as a default
