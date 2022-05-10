import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello from C"

def ff(f):
    print(ctypes.cast(f, FUNTYPE))
    return f()
ff(fun)
</code>
this outputs:
<code>&lt;CFUNCTYPE(None, ...) object at 0x7f4f3b83eb60&gt;
hello from C
</code>

