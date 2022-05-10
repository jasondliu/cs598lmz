import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(ctypes.cast(fun, ctypes.c_void_p).value)
print(hex(id(fun)))
print(hex(id(fun.__call__)))
