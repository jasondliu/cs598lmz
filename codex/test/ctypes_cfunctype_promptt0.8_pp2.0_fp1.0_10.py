import ctypes
# Test ctypes.CFUNCTYPE(*...)(...).
# Python 2 gives TypeError: initializer for ctype 'size_t' must be a integer
# Python 3 gives TypeError: an integer is required (got type Size)
ctypes.c_size_t  # [not-supported]

# Test ctypes.c_void_p(...).
# Python 2 gives TypeError: an integer is required
# Python 3 gives TypeError: an integer is required (got type bytes)
