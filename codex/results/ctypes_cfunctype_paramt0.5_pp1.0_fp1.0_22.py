import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

import numpy as np

class F:
    """
    A class that can be initialized with a function and then called as a
    function.
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self.func(*args)

def f(x, y):
    return x + y

def g(x, y):
    return x - y

if __name__ == '__main__':
    f = F(f)
    g = F(g)
    a = np.array([f, g])
    print(a)
