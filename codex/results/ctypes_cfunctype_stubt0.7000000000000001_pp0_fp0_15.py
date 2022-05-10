import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def fun2(arg):
    return arg

print(fun())
print(fun2(42))
