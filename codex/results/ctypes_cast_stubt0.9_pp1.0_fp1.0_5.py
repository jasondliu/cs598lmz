import ctypes
ctypes.cast(1, ctypes.c_int32)

# Rule for converting class objects.
ctypes.cast(1, int)

# These rules have some shortcomings: ways to crash CPython that should be
# recognised as errors.

ctypes.cast(1, ctypes.c_int32 * ctypes.c_int32)

ctypes.cast(1, ctypes.c_int32 * (ctypes.c_int32 * ctypes.c_int32))


# For example:
#          c_int = ctypes.c_int
#          ctypes.cast(1, c_int)
#          ctypes.cast(1, c_int * ctypes.c_int)
#          ctypes.cast(1, c_int * (c_int * ctypes.c_int))
