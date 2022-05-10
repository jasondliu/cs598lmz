import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class C(ctypes.Structure):
    _fields_ = [('fun', FUNTYPE)]

c = C()
c.fun = fun

print c.fun()
</code>

