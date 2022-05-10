import ctypes
# Test ctypes.CFUNCTYPE()
#
# This tests the new CFUNCTYPE() feature, which allows a ctypes function
# to be used as a callback.
#
# The test is done by creating a C function that takes a callback,
# and then calls it.  The callback is a ctypes function.
#
# The C function also takes a pointer to a function, which is not yet
# supported.  The test should fail if the pointer to function is
# called.

from ctypes import *

# Create a C function that takes a callback.
callback = CFUNCTYPE(c_int, c_int, c_int)
libc = cdll.LoadLibrary(None)

# The C function is called 'myadd'.  It takes 2 ints and a callback.
# It calls the callback with the 2 ints added together, and returns
# whatever the callback returns.
myadd = libc.myadd
myadd.argtypes = [c_int, c_int, callback]
myadd.restype = c_int

# This is the callback.  It adds its 2 arguments and returns the
