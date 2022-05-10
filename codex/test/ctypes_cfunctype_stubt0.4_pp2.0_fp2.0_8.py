import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# but this will fail
@FUNTYPE
def fun():
    return "hello"

print(fun())
