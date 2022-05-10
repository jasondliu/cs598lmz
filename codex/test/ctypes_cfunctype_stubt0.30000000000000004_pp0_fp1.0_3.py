import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert fun() == 1

def fun2():
    return 2

fun3 = FUNTYPE(fun2)
assert fun3() == 2

def fun4(x):
    return x

fun5 = FUNTYPE(fun4)
assert fun5(5) == 5

def fun6(x, y):
    return x + y

fun7 = FUNTYPE(fun6)
assert fun7(5, 6) == 11

def fun8(x, y, z):
    return x + y + z

fun9 = FUNTYPE(fun8)
assert fun9(5, 6, 7) == 18

def fun10(x, y, z, w):
    return x + y + z + w

fun11 = FUNTYPE(fun10)
assert fun11(5, 6, 7, 8) == 26

def fun12(x, y, z, w, v):
    return x + y + z + w + v

fun13 = FUNTYPE(fun12)
