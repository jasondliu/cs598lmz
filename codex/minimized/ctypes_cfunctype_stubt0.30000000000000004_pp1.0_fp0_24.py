import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun3(x, y):
    return x + y
print(fun3(5, 6))
