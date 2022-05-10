import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())
print(fun.__name__)
print(fun.__doc__)

@FUNTYPE
def fun2(x, y):
    return x+y
print(fun2(1, 2))
