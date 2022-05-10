import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2(x):
    return x

@FUNTYPE
def fun3(x, y):
    return x + y

@FUNTYPE
def fun4(x, y, z):
    return x + y + z

@FUNTYPE
def fun5(x, y, z, t):
    return x + y + z + t

@FUNTYPE
def fun6(x, y, z, t, u):
    return x + y + z + t + u

@FUNTYPE
def fun7(x, y, z, t, u, v):
    return x + y + z + t + u + v

@FUNTYPE
def fun8(x, y, z, t, u, v, w):
    return x + y + z + t + u + v + w

@FUNTYPE
def fun9(x, y, z, t, u, v, w, x2):
    return x + y + z + t + u + v + w + x2

@FUNTYPE
def fun10(
