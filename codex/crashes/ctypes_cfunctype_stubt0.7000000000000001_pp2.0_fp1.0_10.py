import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun2(a, b):
    print(a, b)
print(fun2(3, 5))
