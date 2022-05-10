import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    w = ctypes.c_int

a = S()
a.x = 1.0
a.y = 2.0
a.z = 3.0
a.w = 4
print(a)

b = S(1.0, 2.0, 3.0, 4)
print(b)
