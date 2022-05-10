import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 42
@FUNTYPE
def fun2(x, y):
    return x + y
assert fun2(2, 3) == 5
