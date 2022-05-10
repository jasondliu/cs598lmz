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
print(s._fields_)
print(s._asdict())

print(s.x.__dict__)
print(s.y.__dict__)

print(s.x.value)
print(s.y.value)

print(s.x.__class__)
print(s.y.__class__)

print(s.x.__class__.__dict__)
print(s.y.__class__.__dict__)

print(s.x.__class__.__dict__['__get__'])
print(s.y.__class__.__dict__['__get__'])

print(s.x.__class__.__dict__['__set__'])
print(s.y.__class__.__dict__['__set
