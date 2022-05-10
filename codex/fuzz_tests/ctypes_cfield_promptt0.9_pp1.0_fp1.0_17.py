import ctypes
# Test ctypes.CField
from ctypes import _CData, CFuncPtr, _Pointer, CField, Structure
from ctypes import sizeof, POINTER
from ctypes import c_byte, c_int, c_void_p, c_char_p
from ctypes import addressof, memmove
import sys, inspect
from ctypes.test import need_symbol

################################################################
#
# This is a small field object, containg a pointer to a ctypes instance.

class Field(_CData):
    _type_ = "P"
    _length_ = sizeof(c_void_p)

    def __new__(self, obj):
        # assert isinstance(obj, _CData)
        self = _CData.__new__(self, addressof(obj))
        self._obj = obj
        return self

    def __str__(self):
        return str(self._obj)

    def __repr__(self):
        return "Field(%s)" % self._obj

class Test(unittest.TestCase):
    def test(self):

        class
