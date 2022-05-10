import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print(6)
    return 6
print(fun())
type(fun)
</code>
Since <code>fun</code> is a function pointer, it can be passed as an argument:
<code>class example(ctypes.Structure):
    _fields_ = [('ptr', FUNTYPE)]
pyobj = example(fun)
pyobj.ptr()
</code>

