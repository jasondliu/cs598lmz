import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()

@FUNTYPE
def fun2(a,b):
    return a+b

print fun2(1,2)

@FUNTYPE
def fun3(a,b,c):
    return a+b+c

print fun3(1,2,3)

@FUNTYPE
def fun4(a,b,c,d):
    return a+b+c+d

print fun4(1,2,3,4)

@FUNTYPE
def fun5(a,b,c,d,e):
    return a+b+c+d+e

print fun5(1,2,3,4,5)

@FUNTYPE
def fun6(a,b,c,d,e,f):
    return a+b+c+d+e+f

print fun6(1,2,3,4,5,6)

@FUNTYPE
def fun7(a,b,c,d,e,f,g):
    return a+b+c+d+
