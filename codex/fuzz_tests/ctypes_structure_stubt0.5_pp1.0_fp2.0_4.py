import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

a = S()
a.x = 1
a.y = 2
a.z = 3
print(a.x, a.y, a.z)
print(a.__dict__)
print(dir(a))
print(a.__class__)
print(a.__class__.__dict__)
print(a.__class__.__dict__['x'])
print(a.__class__.x)
