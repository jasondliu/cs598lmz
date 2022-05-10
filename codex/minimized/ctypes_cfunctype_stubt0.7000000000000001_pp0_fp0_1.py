import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
class Foo(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]
@FUNTYPE
def fun(obj):
    return obj.contents.n
a = Foo()
fun(a)
