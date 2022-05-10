import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

f = fun()

class C:
    def __init__(self):
        self.f = f

x = C()

def f(x):
    return x

f(x)
