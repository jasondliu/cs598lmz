import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return global_var
cfun = ctypes.cast(fun, FUNTYPE)
print(ctypes.py_object(cfun()))
