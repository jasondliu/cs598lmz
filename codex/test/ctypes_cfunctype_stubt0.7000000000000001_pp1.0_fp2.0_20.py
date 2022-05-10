import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
fun()

def foo(x):
    return x
def boop():
    return foo
foo = boop
