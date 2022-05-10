import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123
fun()

fun.__name__
fun.__doc__

fun.__module__

import types
isinstance(fun, types.FunctionType)

fun.__globals__ is globals()

def foo():
    pass
foo.__closure__

vars(types.FunctionType) # 类型属性

import sys
sys.getrefcount(fun)
