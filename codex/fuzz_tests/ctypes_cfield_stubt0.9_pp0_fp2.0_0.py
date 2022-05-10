import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyField(ctypes.CField):
    _length_ = 2

class SpecialStructure(ctypes.Structure):
    _fields_ = [('items', ctypes.c_int * MyField._length_)]

print SpecialStructure.items._length_
# 2
</code>

