import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
@FUNTYPE
def fun2(f):
    return f()
assert fun2(fun) == "hello"
