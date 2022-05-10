import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)
print(s.x + s.y)

print()

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)
print(s.x + s.y)

print()

class S(ctypes.Structure):
    pass

S._fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
s = S()
s.x = 1
s.y = 2
print(s.x, s.y)
print(s.x + s.y)

print()

class S(ctypes.Structure):
    pass

