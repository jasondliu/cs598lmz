import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class A(object):
    def __init__(self, x):
        self.x = x
    def getx(self):
        return self.x

a = A(42)
