import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 100

fun()

print(fun.__name__)

import inspect
print(inspect.getargspec(fun))

import types
print(isinstance(fun, types.FunctionType))
print(isinstance(fun, types.BuiltinFunctionType))
print(isinstance(fun, types.BuiltinMethodType))
print(isinstance(fun, types.MethodType))
print(isinstance(fun, types.LambdaType))
