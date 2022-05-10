import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
f = FUNTYPE(lambda x: x**2)
f(3)

# or even

def func(x):
    return x**2

ctypes.cast(func, FUNTYPE)

# or even

class Func(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

func = Func(lambda x: x**2)
ctypes.cast(func, FUNTYPE)
</code>

