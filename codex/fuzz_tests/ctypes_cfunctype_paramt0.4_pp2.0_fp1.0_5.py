import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class Func:
    def __init__(self, fun):
        self.fun = FUNTYPE(fun)

def f(x):
    return 2*x

f = Func(f)
print(f.fun(3))
</code>

