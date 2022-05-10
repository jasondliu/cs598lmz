import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

a = S()
a.x = 1
a.y = 2
a.z = 3

b = S()
b.x = 4
b.y = 5
b.z = 6

