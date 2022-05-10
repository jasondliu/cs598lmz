import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun2():
    return 2

def fun3():
    return 3

def fun4():
    return 4

def fun5():
    return 5

def fun6():
    return 6

class A(object):
    def __init__(self):
        self.fun = fun
        self.fun2 = fun2
        self.fun3 = fun3
        self.fun4 = fun4
        self.fun5 = fun5
        self.fun6 = fun6

def main():
    a = A()
