import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
def func(x):
    return math.log(x) + 1.0/x
CFUNC = FUNTYPE(func)
CFUNC(2)

General function:

class MyClass:
    def func(self, x):
        return self.x
obj = MyClass()
obj, func(4)

class Result:
    def __init__(self, val, err):
        self.val = val
        self.err = err
def f(x, y):
    return Result(x / y, 0)

def g(a, b, c, x):
    r1 = f(x, a)
    if r1.err:
        return...
    r2 = f(b, r1.val)
    if r2.err:
        return...
    r3 = f(r2.val, c)
    if r3.err:
        return...
    return Result(r3.val, 0)
"""

# a is a callable object
#
