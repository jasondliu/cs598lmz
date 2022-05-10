import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)

print(s.__dict__['x'])
print(s.__dict__['y'])

print(s.__dict__.keys())

print(s.__dict__.values())

print(s.__dict__.items())

print(s.__dict__.get('x'))
print(s.__dict__.get('y'))

print(s.__dict__.get('z'))

print(s.__dict__.get('z', 'default'))

print(s.__dict__.get('z', None))

print(s.__dict__.get('z', 0))

print(s.__dict__.get('z', []))

print(s.__dict__.get('z', {}))

