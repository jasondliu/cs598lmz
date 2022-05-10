import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.x.__class__)
print(s.y.__class__)

print(s.x.__class__.__name__)
print(s.y.__class__.__name__)

print(s.x.__class__.__module__)
print(s.y.__class__.__module__)

print(s.x.__class__.__bases__)
print(s.y.__class__.__bases__)

print(s.x.__class__.__dict__)
print(s.y.__class__.__dict__)

print(s.x.__class__.__doc__)
