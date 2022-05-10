import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 4

print(fun())

def fun2():
    return 4

print(fun2())
