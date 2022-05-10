import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return 5

fun()

from _ctypes import PyObj_FromPtr
PyObj_FromPtr(id(fun))

from ctypes import CFUNCTYPE, cast, c_int
F = CFUNCTYPE(c_int, c_int, c_int)
def callit(fun, n, m):
    fun = cast(fun, F)
    print(fun(n, m))
callit(id(fun), 1, 2)
</code>

