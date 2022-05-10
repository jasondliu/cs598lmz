import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

print S.x
print S._fields_

print S.x.__get__(S())
print S().x
