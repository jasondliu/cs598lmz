import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

A = S()

A.x = 1
A.y = 2
A.z = 3

print A.x
print A.y
print A.z

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
