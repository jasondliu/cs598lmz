import ctypes
# Test ctypes.CField.from_address()
CField = ctypes.CField

from ctypes import *
from ctypes.test import need_symbol

import _ctypes_test

class X(Structure):
    _fields_ = [
        ("a", c_int)
    ]

class Y(Structure):
    _fields_ = [
        ("b", c_int)
    ]

lib = CDLL(_ctypes_test.__file__)

# Get the address of a global variable
address = lib.glob_intp.value

# This address actually points to a c_int, so the result
# should be a c_int object.
result = c_int.from_address(address)

# the address is stored in the _objects_ attribute, so
# the object is a real object, not a fake one:
assert isinstance(result, c_int)

# the value is correct
assert result.value == 42

# modify the value
result.value = 17
assert result.value == 17

# the value of the global variable changed, too
