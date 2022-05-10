import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

class Func:
    def __init__(self, f):
        self.f = FUNTYPE(f)

    def __call__(self, a, b):
        return self.f(a, b)

f = Func(func)
print(f(1, 2))
</code>

