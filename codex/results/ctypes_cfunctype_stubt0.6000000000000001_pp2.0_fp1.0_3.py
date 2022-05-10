import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

class X(ctypes.Structure):
    _fields_ = [('fun', FUNTYPE),]
x = X()
x.fun = fun

print x.fun()
</code>

