import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class A(object):
    def __init__(self):
        self.fun = fun

a = A()
a.fun()
</code>

