import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
print fun()
</code>
Output:
<code>hello world
</code>
This works on both 32 and 64 bit Windows (tested with py2exe).

