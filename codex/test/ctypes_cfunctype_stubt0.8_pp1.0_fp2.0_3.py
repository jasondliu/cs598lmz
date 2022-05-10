import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2
@FUNTYPE
def fun2():
    return (1, 2)

