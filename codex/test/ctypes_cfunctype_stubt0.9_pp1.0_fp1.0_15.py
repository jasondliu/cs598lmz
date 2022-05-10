import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@FUNTYPE
def fun2(x):
    return x

def foo():
    pass

