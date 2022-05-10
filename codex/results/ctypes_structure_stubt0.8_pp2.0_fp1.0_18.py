import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    _fields_ = [
        ("x", ctypes.c_int, 1),
        ("y", ctypes.c_int, 2),
        ("padding", ctypes.c_int, 29),
    ]

class D(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    _fields_ = [
        ("x", ctypes.c_int, 3),
        ("y", ctypes.c_int, 2),
        ("padding", ctypes.c_int, 27),
    ]

s = S()
s.x = 1
s.y = 2
print("s =", s.x, s.y)

d = ctypes.cast(ctypes.byref(s), ctypes.POINTER(D))
print("d =", d.contents.x, d.contents.y)
</code>
But it works only when <code>s</code> and <code>d</
