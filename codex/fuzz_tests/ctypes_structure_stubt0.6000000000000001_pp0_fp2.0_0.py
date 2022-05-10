import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

print S.x
print S.y
print S.x.offset
print S.y.offset
print S.x.size
print S.y.size
