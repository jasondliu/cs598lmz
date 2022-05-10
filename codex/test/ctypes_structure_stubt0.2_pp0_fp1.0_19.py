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

print(s.__dict__['x'] == s.x)

print(s.__dict__['x'] is s.x)

print(s.__dict__['x'] == 1)

print(s.__dict__['x'] is 1)

print(s.__dict__['x'] == ctypes.c_int(1))

print(s.__dict__['x'] is ctypes.c_int(1))

print(s.__dict__['x'] == ctypes.c_int(1).value)

print(s.__dict__['x'] is ctypes.c_int(1).value)

