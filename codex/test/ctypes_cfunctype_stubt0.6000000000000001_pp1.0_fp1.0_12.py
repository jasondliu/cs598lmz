import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2():
    return 2

class X(object):
    def __init__(self):
        self.fun = fun
        self.fun2 = fun2

class Y(X):
    pass

x = X()
y = Y()

