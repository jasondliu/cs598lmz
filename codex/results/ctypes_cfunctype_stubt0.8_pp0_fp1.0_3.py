import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
ret = fun()

print(str(fun), fun.__name__)
print(ret)
