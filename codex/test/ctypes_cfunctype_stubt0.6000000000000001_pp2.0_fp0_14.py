import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def fun2(x):
    return 2

def fun3(x,y):
    return 3

def fun4(x,y,z):
    return 4

print(fun())
print(fun2(1))
print(fun3(1,2))
print(fun4(1,2,3))
