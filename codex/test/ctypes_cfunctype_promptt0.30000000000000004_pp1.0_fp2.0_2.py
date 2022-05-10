import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

# This test is for the new ctypes.CFUNCTYPE implementation.
#
# The old implementation was very slow, because it created a new
# Python function for each call to CFUNCTYPE.  The new implementation
# is much faster, because it creates a new Python function only once
# per CFUNCTYPE call.

# The following code is used to test the new implementation.  It
# creates a new Python function for each call to CFUNCTYPE.  The
# function is called with a pointer to a structure as argument, and
# the function returns the sum of the structure members.

# This is the structure used by the test.
class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

# This is the Python function used by the test.
def sum(p):
    return p.contents.x + p.contents.y

# This is the C function used by the test.
