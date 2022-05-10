import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

assert ctypes.sizeof(S) == ctypes.sizeof(T)
assert ctypes.sizeof(S) == 2 * ctypes.sizeof(ctypes.c_int)

assert S().x == 0
assert S().y == 0

s = S()
s.x = 1
s.y = 2
assert s.x == 1
assert s.y == 2

t = T()
t.x = 1
t.y = 2
assert t.x == 1
assert t.y == 2

assert S.x.offset == 0
assert S.y.offset == ctypes.sizeof(ctypes.c_int)
assert S.x.size == ctypes.sizeof(ctypes.c_int)
assert S.y.size == ctypes.sizeof(ctypes.c_int
