import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    z = ctypes.c_float()

a = S()
a.x = 2.0
a.z = 2.0
a.x += a.z
print(a.x)
