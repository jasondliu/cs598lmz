import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
cfun = fun.ctypes
</code>
Now, <code>fun</code> is a Python function, but <code>cfun</code> is a <code>ctypes.CFUNCTYPE</code> object. You can call <code>fun</code> and <code>cfun</code> in the same way, but they are not the same object.

