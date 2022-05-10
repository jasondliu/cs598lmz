import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def test_fun():
    assert fun() == 0

@FUNTYPE
def fun2(a):
    return a

def test_fun2():
    assert fun2(1) == 1

@FUNTYPE
def fun3(a, b):
    return a+b

def test_fun3():
    assert fun3(1, 2) == 3

@FUNTYPE
def fun4(a, b, c):
    return a+b+c

def test_fun4():
    assert fun4(1, 2, 3) == 6

@FUNTYPE
def fun5(a, b, c, d):
    return a+b+c+d

def test_fun5():
    assert fun5(1, 2, 3, 4) == 10

@FUNTYPE
def fun6(a, b, c, d, e):
    return a+b+c+d+e

def test_fun6():
    assert fun6(1, 2, 3, 4, 5) == 15

