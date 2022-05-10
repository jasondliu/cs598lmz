import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 4
class A(ctypes.Structure):
    _fields_ = [("f", ctypes.c_int), ("g", ctypes.c_double, (1,2,3))]
fun() + A()
