import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

class A(object):
    def __init__(self):
        self.fun = fun

a = A()
print a.fun()
</code>

