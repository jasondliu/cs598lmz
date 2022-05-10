import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    fun()

def g():
    return f()

def h():
    return g()

