import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.Structure is a subclass of ctypes.Union, so it can be used as a union

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

u = U()
u.x = 1
u.y = 2

print(u.x, u.y)

# ctypes.Structure is a subclass of ctypes.Union, so it can be used as a union

class U(ctypes.Union):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

u = U()
u.x = 1
u.y = 2

print(u.x, u.y)

# ctypes.Structure is a subclass of ctypes.Union, so it can be used as a union
