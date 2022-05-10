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
</code>
Note that I'm using ctypes.Structure here. This is not required, but is a convenient way to bundle the function pointer in a class.

