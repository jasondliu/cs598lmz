import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

tup = (1, 2, 3)
def f(x):
    return tup[x]

class C(object):
    def __init__(self):
        self.x = 42
        self.y = "Hello"
        self.z = self.x + self.y
    def f(self):
        return self.z
    def g(self, c):
        return self.z + c

def f2(x):
    return x + x

def f3(x, y):
    return x + y

def f4(x, y):
    if x == 1:
        return y + y
    else:
        return 0

def f5(x):
    return x

def f6(x):
    return x

def f7(x):
    return x

def f8(x):
    return x

def f9(x, y):
    return x + y

def f10(x, y):
    return x + y

def f11(x,
