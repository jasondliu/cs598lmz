import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = 25
    y = 2
    z = x + y
    a = x % y
    b = y // x
    c = x * y
    d = x - y
    e = x / y
    return [z, a, b, c, d, e]

fun()
