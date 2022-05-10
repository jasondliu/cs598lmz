import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

@FUNTYPE
def fun2():
    return 0

fun2.__module__ = 'foo'
fun2.__name__ = 'baz'

