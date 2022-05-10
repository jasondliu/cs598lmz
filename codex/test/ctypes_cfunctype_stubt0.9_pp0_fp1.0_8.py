import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello from C"

def ff(f):
    print(ctypes.cast(f, FUNTYPE))
    return f()
ff(fun)
