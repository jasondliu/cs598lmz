import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

f = fun()
print(f) # 42
