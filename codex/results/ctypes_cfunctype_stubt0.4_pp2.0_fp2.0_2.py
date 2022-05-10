import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello"

print(fun())
print(fun2())

print(ctypes.cast(fun2, FUNTYPE))
print(ctypes.cast(fun2, FUNTYPE)())
</code>

