import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"
print fun()
</code>
The output is <code>foo</code>

