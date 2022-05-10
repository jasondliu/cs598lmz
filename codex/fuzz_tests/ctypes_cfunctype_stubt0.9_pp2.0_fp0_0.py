import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'OK'

res = ffi.string(ffimod.call_fun(fun))
</code>

