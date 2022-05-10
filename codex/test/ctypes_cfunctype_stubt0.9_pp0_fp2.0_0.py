import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('hi')
    class BadClass(object): pass
    b = BadClass()
    return b

fun()
