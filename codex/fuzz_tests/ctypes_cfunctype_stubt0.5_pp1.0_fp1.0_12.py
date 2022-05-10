import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "Hello"

@FUNTYPE
def fun2(x):
    print x
    return x

@FUNTYPE
def fun3(x, y):
    print x, y
    return x + y

fun3(1, 2)

def fun4(x):
    print x
    return x

fun4(1)

def fun5(x):
    print x
    return x

fun5(1)

def fun6(x, y):
    print x, y
    return x + y

fun6(1, 2)

def fun7(x, y):
    print x, y
    return x + y

fun7(1, 2)

def fun8(x, y):
    print x, y
    return x + y

fun8(1, 2)

def fun9(x, y):
    print x, y
    return x + y

fun9(1, 2)

def fun10(x, y):
    print x, y
    return x + y

fun
