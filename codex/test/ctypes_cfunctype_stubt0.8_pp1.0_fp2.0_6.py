import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Mixed arguments"

def fun():
    return "No arguments"

def fun():
    return "Fixed arguments", "hello"

def fun(arg1, arg2, **args):
    return "Keyword arguments"

def fun(arg1, *args, **kwargs):
    return "Mixed arguments"
