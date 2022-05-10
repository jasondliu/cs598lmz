import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
lib.call_fun(fun)  # prints: function returned 1
</code>

