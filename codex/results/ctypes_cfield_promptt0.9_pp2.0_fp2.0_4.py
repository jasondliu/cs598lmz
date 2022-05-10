import ctypes
# Test ctypes.CField in this module.
import copy
# Test copy.copy(ctypes.CField) in this module.
import collections
# Test implemetation of __len__, __getitem__ and __setitem__.
import bisect
import heapq

if is_cli:
    import System
    from System.Reflection import FieldInfo as Field_info
else:
    import System.Reflection
    Field_info = System.Reflection.FieldInfo

class sized_int(ctypes._SimpleCData):
    _type_ = "i"
    _subtypes_ = []
    _subtype_ = []
    _range = None
    _objects = {}
    def __new__(self, val):
        from _ctypes import sizeof
        self._range = range(-(2**(sizeof(self._type_)*8 - 1)), 2**(sizeof(self._type_)*8 - 1))
        return ctypes.c_int.__new__(self, val)

    def _check_retval_(value):
        if value not in sized_int._range:

