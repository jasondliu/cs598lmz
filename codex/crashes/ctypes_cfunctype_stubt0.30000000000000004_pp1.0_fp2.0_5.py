import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun2(x,y):
    return x+y
cfun = FUNTYPE(fun2)
print(cfun(1,2))
