import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    w = ctypes.c_double

a = S(1,2,3,4)
print a.x
print a.y
print a.z
print a.w
