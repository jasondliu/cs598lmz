import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 3
print fun.__name__
fun()
</code>
If you have issues with the compiler:
<code>&gt;&gt;&gt; ctypes.PyCFuncPtr == ctypes.CFUNCTYPE
True
</code>

