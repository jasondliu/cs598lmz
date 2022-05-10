import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    """Call input() in C"""
    return input("Type something: ")
res = fun()
