import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 0
@FUNTYPE
def fun(x):
    return x
print(fun(2))
