import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2(a):
    return a

assert fun() == 1
assert fun2(3) == 3

@FUNTYPE
def fun3(a, b):
    return a, b

assert fun3(3, 4) == (3, 4)

@FUNTYPE
def fun4(a, b, c):
    return a, b, c

assert fun4(3, 4, 5) == (3, 4, 5)

@FUNTYPE
def fun5(a, b, c, d):
    return a, b, c, d

assert fun5(3, 4, 5, 6) == (3, 4, 5, 6)

@FUNTYPE
def fun6(a, b, c, d, e):
    return a, b, c, d, e

assert fun6(3, 4, 5, 6, 7) == (3, 4, 5, 6, 7)

@FUNTYPE
def fun7(a, b, c, d, e, f):
    return a, b
