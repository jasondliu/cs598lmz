import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint
    _fields_ = [("x", ctypes.c_uint)]

s = S()

b = memoryview(s)

print(b.format)
print(b.itemsize)
print(b.shape)
print(b.strides)

