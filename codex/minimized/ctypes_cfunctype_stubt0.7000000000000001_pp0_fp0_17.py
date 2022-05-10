import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise ValueError
def f(x):
        return fun
f(False)()
