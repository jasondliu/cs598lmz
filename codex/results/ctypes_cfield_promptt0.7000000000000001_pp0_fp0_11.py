import ctypes
# Test ctypes.CField and CField.get_value

import _ctypes_test

# This test crashes, but only if the CField.get_value() method is
# actually called. So, try to access the value of the field, and check
# that nothing bad happens, but no need to check the value.

try:
    dll = ctypes.CDLL(_ctypes_test.__file__)
except WindowsError:
    from _ctypes import LoadLibrary as dll

try:
    c_ubyte = ctypes.c_ubyte
except AttributeError:
    c_ubyte = ctypes.c_byte

class X(ctypes.Structure):
    _fields_ = [("x", c_ubyte)]

dll.my_structure_8.restype = ctypes.POINTER(X)

s = dll.my_structure_8()
print s.contents.x,
print s.contents.x
