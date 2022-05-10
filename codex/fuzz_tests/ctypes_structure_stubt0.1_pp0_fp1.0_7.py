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

print(s.__dict__['x'])

print(s.x)

s.x = 5

print(s.__dict__)

print(s.__dict__['x'])

print(s.x)

print(s.__dict__['x'])

print(s.x)

print(s.__dict__)

print(s.__dict__['x'])

print(s.x)

s.__dict__['x'] = 6

print(s.__dict__)

print
