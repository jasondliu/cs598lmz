import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class C(object):
    def __init__(self):
        self._as_parameter_ = 1

def func(x):
    return x + 1

f = FUNTYPE(func)
assert f(C()) == 2
