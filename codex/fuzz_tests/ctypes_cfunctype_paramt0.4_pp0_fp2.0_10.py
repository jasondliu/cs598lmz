import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class MyFunc:
    def __init__(self, func):
        self.func = FUNTYPE(func)

def test(x):
    return x * x

f = MyFunc(test)
print(f.func(2))
</code>

