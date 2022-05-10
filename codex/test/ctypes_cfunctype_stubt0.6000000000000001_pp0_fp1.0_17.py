import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class A(object):

    def __init__(self):
        self.f = fun

a = A()
