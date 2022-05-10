import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ctypes.py_object(42)

class C(object):
    __slots__ = ['fun']
    fun = FUNTYPE(fun)

C.fun()
</code>

