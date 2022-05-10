import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
</code>
This should be safe since <code>None</code> is a valid return value for a Python function.

