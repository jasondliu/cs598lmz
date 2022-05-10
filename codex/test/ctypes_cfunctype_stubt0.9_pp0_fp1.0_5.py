import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
@FUNTYPE
def fun2():
    return None

print(fun())
print(fun2())


