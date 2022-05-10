import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x, s.y
print s.__dict__
print s.__dict__['x']
print s.__dict__['y']

s.__dict__['x'] = 3
s.__dict__['y'] = 4

print s.x, s.y
print s.__dict__
print s.__dict__['x']
print s.__dict__['y']

print "-" * 20

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2

print s.x, s.y
print s.__dict__
print s.__dict__['x']
print s.__dict__['y']

s.__dict__['x'] = 3
s.__dict__['y'] =
