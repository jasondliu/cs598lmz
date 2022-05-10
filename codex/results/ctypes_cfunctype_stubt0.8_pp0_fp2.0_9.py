import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
try:
    print(fun().value)
except AttributeError:
    print("AttributeError")
print("OK")
