import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test of the ctypes.CFUNCTYPE() factory function.
#
# This test will fail if the return value of the callback function is not
# correctly converted to a Python object.

from ctypes import *

def callback(arg):
    return arg

CALLBACK = CFUNCTYPE(c_int, c_int)

# Create a callback instance
cb = CALLBACK(callback)

# Call the callback and check its result
res = cb(42)

if res != 42:
    raise RuntimeError("CFUNCTYPE test failed")

# Test ctypes.PYFUNCTYPE
#
# This is a test of the ctypes.PYFUNCTYPE() factory function.
#
# This test will fail if the return value of the callback function is not
# correctly converted to a Python object.

from ctypes import *

def callback(arg):
    return arg

CALLBACK = PYFUNCTYPE(c_int, c_int)

# Create a callback instance
cb = CALLBACK
