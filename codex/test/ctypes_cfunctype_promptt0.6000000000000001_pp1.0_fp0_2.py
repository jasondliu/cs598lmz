import ctypes
# Test ctypes.CFUNCTYPE

# The following function uses a function pointer to access a function in a
# shared library.

# On Mac OS X, it seems that the linker doesn't export the symbol unless
# it's actually used, so we need to use it from here.
