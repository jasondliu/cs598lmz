import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 10

print fun()
</code>
and the output is:
<code>10
</code>

