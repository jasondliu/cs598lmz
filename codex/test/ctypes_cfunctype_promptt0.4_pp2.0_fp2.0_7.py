import ctypes
# Test ctypes.CFUNCTYPE()
#
# This test passes if it does not crash.

import ctypes

class X(ctypes.Structure):
    pass

X_p = ctypes.POINTER(X)

# This is a bit tricky: the ctypes.CFUNCTYPE() constructor wants to
# convert the argument types to ctypes types, but X_p is not a ctypes
# type, so we have to pass it as a string.
#
# The following line is equivalent to:
#
#     CFUNCTYPE(X_p, ctypes.c_int)
#
