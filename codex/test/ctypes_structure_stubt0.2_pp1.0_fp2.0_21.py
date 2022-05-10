import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

print(s.__dict__)

print(s.__dict__.keys())

print(s.__dict__.values())

print(s.__dict__.items())

print(s.__dict__.get('x'))

print(s.__dict__.get('z'))

print(s.__dict__.get('z', 'default'))

s.__dict__['z'] = 3

print(s.z)

print(s.__dict__)

print(s.__dict__.keys())

print(s.__dict__.values())

print(s.__dict__.items())

print(s.__dict__.get('x'))

print(s.__dict__.get('z'))

print(s.__dict__.get('z', 'default'))

