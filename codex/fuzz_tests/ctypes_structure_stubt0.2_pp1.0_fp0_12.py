import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print s.x
print s.y

print s.__dict__
print s.__dict__.keys()
print s.__dict__.values()
print s.__dict__.items()

print s.__dict__.has_key('x')
print s.__dict__.has_key('z')

print s.__dict__.get('x')
print s.__dict__.get('z')

print s.__dict__.get('x', 'default')
print s.__dict__.get('z', 'default')

s.__dict__['x'] = 3
print s.x

s.__dict__['z'] = 4
print s.z

print s.__dict__

print s.__dict__.pop('x')
print s.__dict__

print s.__dict__.pop('z', 'default')
print s.__dict__


