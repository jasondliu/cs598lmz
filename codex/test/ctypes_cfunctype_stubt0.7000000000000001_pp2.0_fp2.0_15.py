import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "blah"

fun.argtypes = [ctypes.py_object]
fun.restype = ctypes.py_object

