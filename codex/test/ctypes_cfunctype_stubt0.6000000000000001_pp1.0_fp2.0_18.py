import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def fun2():
    return "World"

fun = ctypes.cast(fun, FUNTYPE)
fun()
