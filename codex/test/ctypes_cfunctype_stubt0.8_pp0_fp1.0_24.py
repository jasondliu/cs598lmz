import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
print(fun())
print(repr(fun))
def fun():
    return 1
print(fun())
print(repr(fun))
@FUNTYPE
def fun(x):
    return x
print(fun(2))
print(repr(fun))
# FAILS
def fun(x):
    return x
print(fun(3))
