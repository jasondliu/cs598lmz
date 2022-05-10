import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

# This should raise an exception.
ctypes.cast(123, ctypes.POINTER(ctypes.c_int))

# The following should return NULL pointers of the various types,
# without raising an exception.
ctypes.cast(None, ctypes.POINTER(ctypes.c_int))
ctypes.cast(None, ctypes.POINTER(S))
ctypes.cast(None, ctypes.POINTER(ctypes.c_char))

# This should raise an exception.
