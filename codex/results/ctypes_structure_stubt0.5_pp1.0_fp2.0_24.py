import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

s = S(1.0, 2.0, 3.0)
print(s.x)
print(s.y)
print(s.z)
print(s)

s = S(1, 2, 3)
print(s.x)
print(s.y)
print(s.z)
print(s)

s = S((1, 2, 3))
print(s.x)
print(s.y)
print(s.z)
print(s)

s = S([1, 2, 3])
print(s.x)
print(s.y)
print(s.z)
print(s)

s = S({'x': 1, 'y': 2, 'z': 3})
print(s.x)
print(s.y)
print(s.z)
print(s)

s = S({'x': 1, 'y': 2})
print(s.x)

