import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun2(a,b):
    return a*b
print(fun2(1,2))
