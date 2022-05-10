import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print s.x
print s.y
print s.z

print s.__dict__
print s.__dict__.keys()
print s.__dict__.values()
print s.__dict__.items()

print s.__dict__['x']
print s.__dict__['y']
print s.__dict__['z']

print s.__dict__.get('x')
print s.__dict__.get('y')
print s.__dict__.get('z')

print s.__dict__.get('a')
print s.__dict__.get('b')
print s.__dict__.get('c')

print s.__dict__.get('a', 'default')
print s.__dict__.get('b', 'default')
print s.__dict__.get('c', 'default')
