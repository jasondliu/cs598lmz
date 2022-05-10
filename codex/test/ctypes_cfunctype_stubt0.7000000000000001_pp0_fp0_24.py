import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return (1,2,3)

assert fun(1,2,3) == (1,2,3)

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

@FUNTYPE
def fun():
    return X(1)

