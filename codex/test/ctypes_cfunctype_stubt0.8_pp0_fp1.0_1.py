import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
def fun2(lib):
    return getattr(lib, "fun")()

fun2.restype = ctypes.py_object
import ctypes
