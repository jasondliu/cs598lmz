import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

def f(x):
    return x*x

def f2(x,y):
    return x*y

def f3(x,y,z):
    return x*y*z

def f4(x,y,z,w):
    return x*y*z*w

