import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    return fun()

class X(object):
    pass

def main():
    for i in xrange(10000):
        f()
    for i in xrange(10000):
        X()

main()
