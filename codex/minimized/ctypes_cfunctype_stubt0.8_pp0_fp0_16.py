import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
@FUNTYPE
def fun2(func):
    return func
print(fun2(fun))
