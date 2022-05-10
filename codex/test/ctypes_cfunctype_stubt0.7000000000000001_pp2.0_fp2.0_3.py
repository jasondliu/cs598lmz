import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@FUNTYPE
def fun2(a):
    return a

@FUNTYPE
def fun3(a,b):
    return a+b

@FUNTYPE
def fun4(a,b,c):
    return a+b+c

@FUNTYPE
def fun5(a,b,c,d):
    return a+b+c+d

@FUNTYPE
def fun6(a,b,c,d,e):
    return a+b+c+d+e


def fun7():
    return "hello"

def fun8(a):
    return a

def fun9(a,b):
    return a+b

def fun10(a,b,c):
    return a+b+c

def fun11(a,b,c,d):
    return a+b+c+d

def fun12(a,b,c,d,e):
    return a+b+c+d+e

