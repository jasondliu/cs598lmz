import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello")
    return None

@FUNTYPE
def fun2():
    return some_default_value

print("fun id", id(fun))
print("fun2 id", id(fun2))
print("fun is fun2:", fun is fun2)
