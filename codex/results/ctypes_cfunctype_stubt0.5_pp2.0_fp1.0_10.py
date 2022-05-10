import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
assert fun() == 42
</code>
Note that you can't return a <code>ctypes.c_int</code> from a <code>CFUNCTYPE</code> function.  It must be a Python object.

