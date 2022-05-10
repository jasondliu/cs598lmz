import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class S2(ctypes.Structure):
    _fields_ = [("offset", ctypes.c_int),
                ("size", ctypes.c_int),
                ("size2", ctypes.c_int)]

def f(a, b):
    if a.value > b.value:
        return -(a.value + b.value)
    if a.value == b.value:
        return a.value
    return a.value + b.value

class C(object):
    def __init__(self, x):
        self.x = x

    def f(self, a, b):
        if a.value > b.value:
            return -(a.value + b.value)
        if a.value == b.value:
            return a.value
        return a.value + b.value

    def f_no_args(self):
        return self.x

