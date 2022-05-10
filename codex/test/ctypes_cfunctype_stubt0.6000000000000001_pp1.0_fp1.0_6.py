import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class A(object):
    pass

def f():
    a = A()
    a.x = fun
    return a.x

