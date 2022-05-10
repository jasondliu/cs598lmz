import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print type(fun)
print fun()
</code>
output:
<code>&lt;type '_ctypes.PyCFuncPtrType'&gt;
42
</code>

