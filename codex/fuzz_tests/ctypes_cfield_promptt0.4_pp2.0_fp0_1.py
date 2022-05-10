import ctypes
# Test ctypes.CField.from_address()

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()

x.a = 3
x.b = 4

addr = ctypes.addressof(x)

fld = ctypes.CField.from_address(addr, ctypes.c_int, "a")
assert fld.offset == 0
assert fld.size == ctypes.sizeof(ctypes.c_int)
assert fld.name == "a"
assert fld.type == ctypes.c_int

fld = ctypes.CField.from_address(addr, ctypes.c_int, "b")
assert fld.offset == ctypes.sizeof(ctypes.c_int)
assert fld.size == ctypes.sizeof(ctypes.c_int)
assert fld.name ==
