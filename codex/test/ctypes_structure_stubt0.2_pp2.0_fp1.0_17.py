import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

s = S(1, 2)
print(s.x, s.y)

s = S(x=1, y=2)
print(s.x, s.y)

s = S(y=2, x=1)
print(s.x, s.y)

s = S(1)
print(s.x, s.y)

s = S(1, y=2)
print(s.x, s.y)

s = S(x=1)
print(s.x, s.y)

s = S(y=2)
print(s.x, s.y)

