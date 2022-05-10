import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class Foo(ctypes.Structure):
    _fields_ = [("bar", FUNTYPE)]

foo = Foo(fun)
print(foo.bar())
</code>

