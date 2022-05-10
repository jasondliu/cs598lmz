import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun1(x,y):
    return x+y
functype = FUNTYPE(fun1)
print(functype(1,2))
