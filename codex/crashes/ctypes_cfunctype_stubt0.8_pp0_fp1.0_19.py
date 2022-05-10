import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return "Hello"
@FUNTYPE
def newfun(x):
    return x + " World"
newfun('Hello')
