import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    import sys
    return sys.platform

@FUNTYPE
def fun2(i):
    return i * 2

@FUNTYPE
def fun3(i, j):
    return i * j

@FUNTYPE
def fun4(i, j, k):
    return i * j * k

@FUNTYPE
def fun5(i, j, k, l):
    return i * j * k * l

@FUNTYPE
def fun6(i, j, k, l, m):
    return i * j * k * l * m

@FUNTYPE
def fun7(i, j, k, l, m, n):
    return i * j * k * l * m * n

@FUNTYPE
def fun8(i, j, k, l, m, n, o):
    return i * j * k * l * m * n * o

@FUNTYPE
def fun9(i, j, k, l, m, n, o, p):
    return i * j * k * l * m * n * o * p

@FUN
