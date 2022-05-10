import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
x = fun()
def handle_return_int(value):
    return x.rget()
globals()["a"] = handle_return_int
