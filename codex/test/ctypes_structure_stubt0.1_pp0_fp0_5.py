import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

print(s.__dict__)

print(s.__dict__['x'])

s.__dict__['x'] = 4

print(s.x)

print(s.__dict__)

s.__dict__['a'] = 5

print(s.__dict__)

print(s.a)

print(s.__dict__['a'])

