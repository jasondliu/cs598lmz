import ctypes
# Test ctypes.CFUNCTYPE

def func(x, y):
    return x * y

class X(object):
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
        return self.x * y

class Y(object):
    def __call__(self, x, y):
        return x * y

def test_CFUNCTYPE():
    for proto in [ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int),
                  ctypes.CFUNCTYPE(ctypes.c_int, (ctypes.c_int, ctypes.c_int)),
                  ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
                  ctypes.CFUNCTYPE(ctypes.c_int, (ctypes.c_int,))]:
        f = proto(func)
        assert f(2, 3) == 6
        f = proto(lambda x, y: x * y)
