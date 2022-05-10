import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

class A(object):
    def __init__(self):
        self.x = fun

a = A()
