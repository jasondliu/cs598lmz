import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return []
class A(object):
    pass
a = A()
a.__add__ = fun
