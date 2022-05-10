import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

# ctypes.Structure is a subclass of ctypes.Union, so we can use it in the same way

class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

u = U()
u.x = 1
u.y = 2
u.z = 3

print(u.x, u.y, u.z)

# ctypes.Structure and ctypes.Union can also be used to create C-compatible structures and unions

