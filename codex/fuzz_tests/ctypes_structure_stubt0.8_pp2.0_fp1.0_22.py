import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    xx = ctypes.c_int # duplicate

print S.x
print S._fields_
