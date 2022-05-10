import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class X(object):
    def __init__(self):
        pass
    
    fun = fun

x = X()

class Y(X):
    def __init__(self):
        pass

y = Y()

print x.fun()
print y.fun()
