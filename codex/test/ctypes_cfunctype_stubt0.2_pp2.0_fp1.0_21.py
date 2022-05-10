import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@FUNTYPE
def fun2(a):
    return a

@FUNTYPE
def fun3(a, b):
    return a, b

@FUNTYPE
def fun4(a, b, c):
    return a, b, c

@FUNTYPE
def fun5(a, b, c, d):
    return a, b, c, d

@FUNTYPE
def fun6(a, b, c, d, e):
    return a, b, c, d, e

@FUNTYPE
def fun7(a, b, c, d, e, f):
    return a, b, c, d, e, f

@FUNTYPE
def fun8(a, b, c, d, e, f, g):
    return a, b, c, d, e, f, g

@FUNTYPE
def fun9(a, b, c, d, e, f, g, h):
    return a, b, c, d, e, f, g, h

