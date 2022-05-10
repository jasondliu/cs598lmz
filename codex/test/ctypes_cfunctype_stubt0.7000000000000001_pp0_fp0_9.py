import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2

class A(object):
    def fun(self):
        return 3

class B(object):
    def fun(self, a):
        return a

