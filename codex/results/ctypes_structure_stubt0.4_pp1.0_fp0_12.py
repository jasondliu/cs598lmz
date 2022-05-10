import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', x), ('x', x)]

print S.x
print S._fields_
