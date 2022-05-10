import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2(x):
    return x+1

@FUNTYPE
def fun3(x, y):
    return x + y

@FUNTYPE
def fun4(x, y, z):
    return x + y + z

@FUNTYPE
def fun5(x, y, z, w):
    return x + y + z + w

@FUNTYPE
def fun6(x, y, z, w, v):
    return x + y + z + w + v

@FUNTYPE
def fun7(x, y, z, w, v, u):
    return x + y + z + w + v + u

@FUNTYPE
def fun8(x, y, z, w, v, u, t):
    return x + y + z + w + v + u + t

@FUNTYPE
def fun9(x, y, z, w, v, u, t, s):
    return x + y + z + w + v + u + t + s

