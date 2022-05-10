import ctypes
# Test ctypes.CFUNCTYPE's memmove function.
libc = ctypes.CDLL("libc.so.6")
try:
    memmove = libc.memmove
except AttributeError:
    raise SkipTest("skipping test due to missing symbol")

# On Windows, memmove has a return type of 'int'.  Make sure that
# this is described as a 'c_int' instance.
if memmove.argtypes is None:
    memmove.argtypes = (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t)
if memmove.restype is None:
    memmove.restype = ctypes.c_int

# We need to pass a non-trivial 'length' argument to the memmove
# function.  This prints '0' if the memmove function works (at least
# in the trivial case)
retval = memmove(0, 0, 1)
assert retval == 0

# If this doesn't raise an exception, the memmove function works.
memmove.argtypes = None
memmove.rest
