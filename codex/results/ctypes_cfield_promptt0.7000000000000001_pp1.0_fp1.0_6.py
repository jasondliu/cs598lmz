import ctypes
# Test ctypes.CField
#
# Set up and tear down some structure types to test passing
# C fields between Python and C.
#

from ctypes import *
from ctypes.test import need_symbol

class X(Structure):
    _fields_ = [("a", c_int),
                ("b", c_float),
                ("c", c_double)]

class Y(Structure):
    _fields_ = [("next", POINTER(Y)),
                ("x", X)]

# the main program
if __name__ == "__main__":
    import _ctypes_test
    lib = CDLL(_ctypes_test.__file__)
    lib.field_in_C.restype = POINTER(Y)

    # Create a structure with a field in it
    x = X(1, 2, 3)
    # Pass the field to C
    y = lib.field_in_C(x)
    # Test the results
    if y.contents.x.a != 1 or \
       y.contents.x.b != 2 or \
       y
