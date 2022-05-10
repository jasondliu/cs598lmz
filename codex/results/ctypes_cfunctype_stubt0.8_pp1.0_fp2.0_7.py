import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hubbabubba"
# this is a function which returns function:
def generator():
    return fun
