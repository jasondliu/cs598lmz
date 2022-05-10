import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def add_x(x, y):
    return x + y

def setup():
    global f
    f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(add_x)
    global s
    s = S()


def loop():
    for i in xrange(10000):
        f(2)
    for i in xrange(10000):
        s.x
    for i in xrange(10000):
        s.x = 1
