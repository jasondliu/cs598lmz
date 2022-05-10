import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class C(object):
    def __init__(self):
        self.fun = fun

c = C()

def f(c):
    return c.fun

def g(c):
    return c.fun()

