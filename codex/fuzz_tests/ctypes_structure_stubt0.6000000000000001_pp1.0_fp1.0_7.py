import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_float

p = ctypes.POINTER(S)

a = S(1, 2)

b = p()
b.contents = a
print(b.contents.x)
