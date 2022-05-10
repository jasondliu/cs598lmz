import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()

s.x = 1
s.y = 2
s.z = 3

print s.x, s.y, s.z

print s.__dict__

print s.__class__

print s.__class__.__dict__

print s.__class__.__dict__['x']

print s.__class__.__dict__['x'].__get__(s)

print s.__class__.__dict__['x'].__get__(s, S)

print s.__class__.__dict__['x'].__get__(s, S) == s.x

print s.__class__.__dict__['x'].__set__(s, 5)

print s.x

print s.__class__.__dict__['x'].__set__(s, 6)

print s.x
