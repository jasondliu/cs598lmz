import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun(a):
    return a
f = FUNTYPE(fun)
result = f(3)
