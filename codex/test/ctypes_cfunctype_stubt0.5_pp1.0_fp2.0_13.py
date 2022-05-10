import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

@FUNTYPE
def fun2(x):
    return x

@FUNTYPE
def fun3(x,y):
    return x+y

@FUNTYPE
def fun4(x,y,z):
    return x+y+z

@FUNTYPE
def fun5(x,y,z,a):
    return x+y+z+a

@FUNTYPE
def fun6(x,y,z,a,b):
    return x+y+z+a+b

@FUNTYPE
def fun7(x,y,z,a,b,c):
    return x+y+z+a+b+c

@FUNTYPE
def fun8(x,y,z,a,b,c,d):
    return x+y+z+a+b+c+d

@FUNTYPE
def fun9(x,y,z,a,b,c,d,e):
    return x+y+z+a+b+c+d+e

