import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = ctypes.c_int(1)
    return x
</code>
You get:
<code>&gt;&gt;&gt; fun()
c_long(1)
</code>

