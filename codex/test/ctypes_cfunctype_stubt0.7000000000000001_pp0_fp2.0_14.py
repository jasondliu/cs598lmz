import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class A():
    def __init__(self):
        self.x = 1

a = A()
a.fun = fun

a.fun()
