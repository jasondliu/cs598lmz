import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int)]

val = C(5, 4, 3)

assert val.a == 5
assert val.b == 4
assert val.c == 3


class B(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('base', B),
                ('c', ctypes.c_int)]

val = C(B(1, 2), 3)

assert val.base.a == 1
assert val.base.b == 2
assert val.c == 3

class C(ctypes.Structure):
    _fields_ = [('base', B),
                ('c', ctypes.c_int)]

    def __init__(self, val):
        self.base.a =
