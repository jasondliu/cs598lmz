import ctypes
# Test ctypes.CFUNCTYPE.

# TODO: double, float, restypes, more than one argument

CALLBACK_FUNC = ctypes.CFUNCTYPE(ctypes.c_int)

