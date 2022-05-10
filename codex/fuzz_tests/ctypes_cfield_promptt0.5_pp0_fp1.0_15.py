import ctypes
# Test ctypes.CField.from_address()
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

a = X()
a.a = 10

f = ctypes.CField.from_address(a, a._fields_[0])

print(f)
print(f.value)
print(f.value == 10)
# Test ctypes.CField.from_address()
from ctypes import *

class X(Structure):
    _fields_ = [("a", c_int)]

a = X()
a.a = 10

f = ctypes.CField.from_address(a, a._fields_[0])

print(f)
print(f.value)
print(f.value == 10)

# Check that we can use ctypes.CField.from_address() to create a
# ctypes.CField instance for a field that is not part of a structure.

f = ctypes.CField.from_address(None, ctypes.Field(None, c_int, "
