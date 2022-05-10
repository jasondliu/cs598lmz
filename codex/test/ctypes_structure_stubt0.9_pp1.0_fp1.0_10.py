import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float
    y = ctypes.c_char

a = S(x=1, y='a')
print(a.x, a.y)
