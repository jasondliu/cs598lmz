import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def main(n):
    for i in xrange(n):
        h()

