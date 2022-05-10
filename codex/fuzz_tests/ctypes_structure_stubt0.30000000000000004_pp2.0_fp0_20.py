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
print s._fields_

print s.__class__
print s.__class__.__dict__
print s.__class__.__dict__['x']
print s.__class__.__dict__['x'].__get__(s, s.__class__)
print s.__class__.__dict__['x'].__set__(s, 3)
print s.x
print s.__class__.__dict__['y'].__get__(s, s.__class__)
print s.__class__.__dict__['y'].__set__(s, 4)
print s.y

print s.__class__.__dict__['x'].__get__(s, s.__class__)
print s.__class__.__dict__['y'].__get__(s, s.__class
