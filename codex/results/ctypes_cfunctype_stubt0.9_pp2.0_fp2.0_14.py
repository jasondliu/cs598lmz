import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 7

@jit
def g2(x):
    def f(y):
        return x + y
    return f

@jit
def g(x):
    return lambda y: x + y

def g3():
    @jit
    def f(y):
        return x + y
    return f

# Utility functions
def do(func):
    res = func()
    print "Result", res, type(res)
    return res
def check(func):
    res = do(func)
    if res != 7:
        raise Exception("got %r; wanted 7" % (res,))

check(fun)
check(g(3))
check(g2(3))
check(g3())
