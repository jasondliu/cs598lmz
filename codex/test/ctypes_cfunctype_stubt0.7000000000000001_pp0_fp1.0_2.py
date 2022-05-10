import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
class A(ctypes.Structure):
    _fields_ = [("fun", FUNTYPE)]
a = A(fun)
res = a.fun()
print(res, type(res))
