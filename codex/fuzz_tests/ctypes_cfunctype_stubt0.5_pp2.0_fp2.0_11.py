import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
print fun()
</code>
The output of this is:
<code>hello world
</code>

