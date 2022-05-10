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

print(s.__dict__.keys())

print(s.__dict__.values())

print(s.__dict__.items())

print(s.__dict__.get('x'))

print(s.__dict__.get('a'))

print(s.__dict__.get('a', 'not found'))

print(s.__dict__.get('a', 'not found'))

print(s.__dict__.get('a', 'not found'))

print(s.__dict__.get('a', 'not found'))

print(s.__dict__.get('a', 'not found'))

