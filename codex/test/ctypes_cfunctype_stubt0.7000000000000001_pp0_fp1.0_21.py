import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
assert fun() == 42

@FUNTYPE
def fun():
    return "hello"
assert fun() == "hello"

