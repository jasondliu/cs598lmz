import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s)

print(s.__dict__)

print(s.__class__)

print(s.__class__.__dict__)

print(s.__class__.__dict__['x'])

print(s.__class__.__dict__['x'].__get__(s))

print(s.__class__.__dict__['x'].__set__(s, 3))

print(s.x)

print(s.__class__.__dict__['x'].__get__(s))

print(s.__class__.__dict__['x'].__delete__(s))

print(s.x)

print(s.__class__.__dict__['x'].__get__(s))

print(s.__class__.__dict__['x'
