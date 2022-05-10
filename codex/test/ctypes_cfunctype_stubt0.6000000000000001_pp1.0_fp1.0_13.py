import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello World")
    return None

print(type(fun))
print(type(fun()))
print(type(fun.__call__()))
