import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class FuncWrapper(object):

    def __init__(self, f):
        self.f = f
        self.func = FUNTYPE(f)

    def __call__(self, x):
        return self.func(x)

class FuncWrapper2(object):

    def __init__(self, f):
        self.f = f
        self.func = FUNTYPE(f)

    def __call__(self, x):
        return self.func(x)


def test_func_wrapper():
    x = 1.0
    f = lambda x: x**2
    g = FuncWrapper(f)
    assert g(x) == f(x)

def test_func_wrapper2():
    x = 1.0
    f = lambda x: x**2
    g = FuncWrapper2(f)
    assert g(x) == f(x)

def test_func_wrapper_and_wrapper2():
    x = 1.0

