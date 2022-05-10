import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a bit tricky, because we need to use a ctypes callback
# function as the callback for another ctypes callback function.
#
# In this test, we use a C callback function that is called by
# the Python callback function.  The C callback function calls
# the Python callback function.  This is done in order to test
# that the Python callback function can be called from C code.

from ctypes import *

# This is the Python callback function.
def py_callback_func(a, b, c):
    print("py_callback_func(%r, %r, %r)" % (a, b, c))
    # Call the C callback function.
    return c_callback_func(a, b, c)

# This is the C callback function.
c_callback_func = CFUNCTYPE(c_int, c_int, c_int, c_int)(
    lambda a, b, c: a + b + c)

# This is the C function that will call the Python callback function.
