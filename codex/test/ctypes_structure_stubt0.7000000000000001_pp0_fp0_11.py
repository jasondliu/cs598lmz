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
b.x = a.x
b.y = a.y
b.z = a.z

print(a, b)
print(a.x, b.x)
print(a.y, b.y)
print(a.z, b.z)
