import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class MyClass(ctypes.Structure):
    _fields_ = [("f", FUNTYPE)]

mc = MyClass()
mc.f = fun
mc.f()
</code>

