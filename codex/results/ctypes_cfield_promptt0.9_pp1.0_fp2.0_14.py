import ctypes
# Test ctypes.CField.from_address
from ctypes import *
from ctypes.test import need_symbol

self = CDLL(self.__file__)

# This field is located at the same address as the "base" argument
# to the function.
# We do all tests with a structure containing a float and a pointer
# float * float
class S(Structure):
    _fields_ = [("b", c_float), ("p", POINTER(c_float))]

NeedsPointer = S

def test_from_address(type_registered):
    if not type_registered:
        return
    s = self.foo0.resuiretypes()
    f = CField.from_address(s, 0)
    assert getattr(s, f.name) == 10.5
    assert f.offset == 0
    assert f.size == sizeof(c_float)

    s = self.foo1.resuiretypes()
    assert getattr(s, "b") == 11.5
    f = CField.from_address(s, sizeof(c_float))

