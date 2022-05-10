import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 4

def f(b):
    if b:
        return (1,2)
    else:
        return lambda: 4

a = f(1)
print(f(1)[0])
print(f(1)[0])
