import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    return fun()

def g():
    for i in range(10):
        f()

g()
