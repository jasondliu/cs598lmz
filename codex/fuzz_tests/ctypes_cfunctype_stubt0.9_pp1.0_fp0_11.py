import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print(1)

f = ctypes.cast(fun, ctypes.CFUNCTYPE(ctypes.c_int))
f()
