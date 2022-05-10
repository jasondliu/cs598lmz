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

assert fun() == X(1)

# this should not segfault
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.POINTER(ctypes.c_int))]

@FUNTYPE
def fun():
    return X(None)

assert fun() == X(None)

x = X(None)
x.x

print("passed all tests..")
