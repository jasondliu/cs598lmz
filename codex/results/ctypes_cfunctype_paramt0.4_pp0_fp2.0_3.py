import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

func_c = FUNTYPE(func)

class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        return self.func(x)

test = Test(func_c)

print test(2)
</code>

