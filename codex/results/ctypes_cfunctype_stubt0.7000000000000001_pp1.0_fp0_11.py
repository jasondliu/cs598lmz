import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
print(fun()())
</code>
The <code>@FUNTYPE</code> wrapper is necessary because calling <code>fun</code> directly would return an integer, instead of an object that can be called.

