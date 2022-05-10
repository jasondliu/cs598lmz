import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 10

fun.__name__ = "name"
import dis
dis.dis(fun)
