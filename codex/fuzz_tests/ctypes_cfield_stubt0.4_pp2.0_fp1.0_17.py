import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def run(func, arg):
    t0 = time.time()
    for i in xrange(1000000):
        func(arg)
    t1 = time.time()
    return t1 - t0

print run(f, 1)
print run(g, 1.0)
print run(h, C())
print run(f, S())
