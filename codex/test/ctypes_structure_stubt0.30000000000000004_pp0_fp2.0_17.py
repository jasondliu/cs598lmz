import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(s):
    s.x = 1
    s.y = 2

s = S()
f(s)
print(s.x, s.y)

# ctypes.Structure is a subclass of ctypes.Union, so it can be used as a union.
# However, the ctypes.Structure class does not support the _fields_ attribute
# that is used to define the fields of a union.

class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

u = U()
u.x = 1
print(u.x, u.y)

# The ctypes.Union class does not support the _pack_ attribute that is used to
# specify the alignment of a structure.

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
