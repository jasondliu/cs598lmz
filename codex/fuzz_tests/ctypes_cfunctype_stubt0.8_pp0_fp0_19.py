import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

fun()
</code>

If you really want to return <code>None</code> from a callback, then use <code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)</code> and then return 0 for <code>None</code>.

